
/**
 *微博的model类
 */
var mongodb=require("./db");
//moment
var moment = require('moment');
function Post(username,post,time,id){
    console.log('come here:'+post);
    this.user=username;
    this.post=post;
    this._id = id;
    //如果时间为空则设置为当前时间
    if(time){
        this.time=time;
    }else{
        //use moment format
        this.time=moment().format('YYYY-MM-DD HH:mm:ss');
    }
}

//读取指定用户下的微博信息
Post.find=function(username,callback){
    mongodb.open(function(err,db){
        if(err){
            return callback(err);
        }
        //读取posts文档
        db.collection("posts",function(err,collection){
            if(err){
               mongodb.close();
                return callback(err);
            }
            //查找user属性为username的文档，如果为null则全部匹配
            var query={};
            if(username){
                query.user=username;
            }
            //按时间排序，并转成数组
            collection.find(query).sort({time:-1}).toArray(function(err,docs){
                mongodb.close();
                if(err){
                    callback(err,null);
                }
                //封装posts为Post对象
                var posts=[];
                docs.forEach(function(doc,index){
                    var post=new Post(doc.user,doc.post,doc.time,doc._id);
                    posts.push(post);
                });
                callback(null,posts);
            });
        });
    });
};
module.exports=Post;
/**
 * 保存操作
 * @param callback
 */
Post.prototype.save=function save(callback){
    //存入mongodb的文档
    var post={
        user:this.user,
        post:this.post,
        time:this.time
    };
    mongodb.open(function(err,db){
        if(err){
            return callback(err);
        }
        //读取posts集合
        db.collection("posts",function(err,collection){
            if(err){
                mongodb.close();
                return callback(err);
            }
            //为user属性添加索引
            collection.ensureIndex("user");
            collection.insert(post,{safe:true},function(err){
                mongodb.close();
                return callback(err,post);
            });
        });
    });
};
/**
 * 删除博客信息
 * @param callback
 */
Post.prototype.deleteBlog = function(callback,post){
    //需要删除的post对象
    mongodb.open(function(err,db){
        if(err){
            return callback(err);
        }
        //删除当前文档
        db.collection('posts',function(err,collection){
            if(err){
                mongodb.close();
                return callback(err);
            }
            //ObjectID类型的field进行删除方法
            var ObjectID = require('mongodb').ObjectID;
            console.log('post._id:'+post._id);
            var obj_id = new ObjectID(post._id);
            console.log('obj_id:'+obj_id);
            //删除当前post
            collection.remove({"_id":obj_id}, {safe:true},function(err,count){
                mongodb.close();
                console.log('count:'+count);
                return callback(err,count);
            });
        });
    });
}