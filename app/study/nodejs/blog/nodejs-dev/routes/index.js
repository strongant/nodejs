
//用于用户密码加密
var crypto = require('crypto');
//导入用户模块
var User= require('../models/User');
//导入Post模块
var Post = require('../models/post');

exports.index = function(req, res){
  Post.find(null,function(err,posts){
    if(err){
      posts = [];
    }
    res.render("index",{
            title:"首页",
            posts:posts
        });
  });
};
//user detail
exports.user=function(req,res){
  User.find(req.params.user,function(err,user){
    if(!user){
      req.session.error = 'the user is not in';
      return res.redirect('/');
    }
    Post.find(user.name,function(err,posts){
      if(err){
        req.session.error = err;
        return redirect('/');
      }
      res.render('user',{
        title:user.name,
        posts:posts,
        name:user.name
      });
    });
  });
};
//save user's message
exports.post=function(req,res){
    var currentUser = req.session.user;
    var post = new Post(currentUser.name,req.body.post);
    post.save(function(err){
      if(err){
        req.session.error = err;
        return res.redirect('/');
      }
      req.session.success =  '发表成功';
      return res.redirect('/u/'+currentUser.name);
    });

};

/**
 * 删除用户发布的微博信息
 * @param req
 * @param res
 */
exports.deleteBlog =  function(req,res){
  var currentUser = req.session.user;
  if(!currentUser){
    req.session.error = '当前用户没有登陆，请登陆后执行此操作';
    return res.redirect("/");
  }
  //构造需要删除的blog对象
  var post = new Post(null,null,null,req.params.id);
  console.log('post:'+post._id);
  post.deleteBlog(function(err,count){
    console.log('err: '+err);
    console.log('delete ok count:'+count);
    if(err){
      req.session.error = err;
      return res.redirect('/');
    }
    req.session.success = '删除博客信息成功';
    return res.redirect('/u/'+currentUser.name);
  },post);
}

/**
 * 跳转注册页面
 * @param req
 * @param res
 */
exports.reg=function(req,res){
    res.render('reg', { title: "注册页面"});
};
/**
 * 注册操作
 * @param req
 * @param res
 * @return {*}
 */
exports.doReg=function(req,res){
  console.log('come--doReg');
  //验证用户输入的口令是否一致
  if(req.body['password']!=req.body['password-repeat']){
    req.session.error = "两次输入的口令不一致";
    return res.redirect('/reg');
  }
  console.log('username:'+req.body.username);
  console.log('password:'+req.body['password']);
  console.log('password-repeat:'+req.body['password-repeat']);
  //生成口令的散列值，我们使用MD5加密
  var md5 = crypto.createHash('md5');
  var password = md5.update(req.body.password).digest('base64');
  //声明需要添加的用户
  var newUser = new User({
    name:req.body.username,
    password:password
  });

  User.find(newUser.name,function(err,user){
    //如果用户已经存在
    if(user){
      req.session.error = '该用户已经存在';
      return res.redirect('/reg');
    }
    //如果不存在则进行添加用户
    newUser.save(function(err){
      if(err){
        req.session.error = err;
        return res.redirect('/reg');
      }
      req.session.user = newUser;
      req.session.success = '注册成功';
      res.locals.user = newUser;
      res.redirect('/');
    });
  });
};
/**
 * 跳转登录页面
 * @param req
 * @param res
 */
exports.login=function(req,res){
    res.render('login', { title: "登录页面"});
};
/**
 * 登录操作
 * @param req
 * @param res
 */
exports.doLogin=function(req,res){
  //check user
  var md5 = crypto.createHash('md5');
  var password = md5.update(req.body.password).digest('base64');
  User.find(req.body.username,function(err,user){
    //check username
    if(!user){
      req.session.error = 'this user is not in ';
      return res.redirect('/login');
    }
    //check password
    if(user.password!=password){
      req.session.error = 'user password is error';
      return res.redirect('/login');
    }
    req.session.user = user;
    req.session.success = "login success";
    res.redirect('/');
  });
};
/**
 * 退出操作
 * @param req
 * @param res
 */
exports.logout=function(req,res){
    req.session.user = null;
    req.session.success = 'login out success';
    return res.redirect('/');
};
