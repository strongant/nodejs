/**
 * Created by bwh on 15-9-25.
 */
//测试使用PhantomJS进行抓取网页截图
var page = require('webpage').create(),
    system = require('system'),
    t, address;
// 如果命令行没有给出网址
if (system.args.length === 1) {
    console.log('Usage: page.js <some URL>');
    phantom.exit();
}
t = Date.now();
address = system.args[1];
page.open(address, function (status) {
    if (status !== 'success') {
        console.log('FAIL to load the address');
    } else {
        t = Date.now() - t;
        console.log('Loading time ' + t + ' ms');
    }
    phantom.exit();
});


