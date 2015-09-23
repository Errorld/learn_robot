
   

# 学习网络爬虫（2）
标签（空格分隔）： 爬虫
---
[英文原文](http://www.voidspace.org.uk/python/articles/urllib2.shtml#openers-and-h
andlers)
##1. info and geturl
urlopen 返还的response 有两个有用的方法：info 和 geturl.
- geturl - 返回抓取到的真正地址。在遇到重定向时有用`304`
- info - 返回response 的headers ，是一个dict
> Typical headers include 'Content-length', 'Content-type', and so on. See the 
Quick Reference to HTTP Headers for a useful listing of HTTP headers with brief 
explanations of their meaning and use.
##2. Openers and Handlers
urllib.request.urlopen 打开URL时使用了默认的opener，opener通过handler工作
可以自己创建opener来使用特定的handler
下面以基本认证为例@urllib_6.py
![](http://7xlyu9.com1.z0.glb.clouddn.com/15-9-23/269672.jpg)
drliunt     发布    新文稿         
    
学习网络爬虫（2）

爬虫

英文原文

1. info and geturl

urlopen 返还的response 有两个有用的方法：info 和 geturl.

geturl - 返回抓取到的真正地址。在遇到重定向时有用304

info - 返回response 的headers ，是一个dict

Typical headers include 'Content-length', 'Content-type', and so on. See the Quick Reference to HTTP Headers for a useful listing of HTTP headers with brief explanations of their meaning and use.
2. Openers and Handlers

urllib.request.urlopen 打开URL时使用了默认的opener，opener通过handler工作 
可以自己创建opener来使用特定的handler

下面以基本认证为例@urllib_6.py 


状态401，response headers中包含WWW-Authenticate: Basic realm="MERCURY Wireless N Router MW310R"

import urllib.request
# create a password manager
password_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()
# Add the username and password.
username = 'admin'  #家里路由器的默认用户名密码
password = 'admin'
# If we knew the realm, we could use it instead of ``None``.
top_level_url = "http://192.168.1.1"
password_mgr.add_password(None, top_level_url, username, password)
handler = urllib.request.HTTPBasicAuthHandler(password_mgr)
# create "opener" (OpenerDirector instance)
opener = urllib.request.build_opener(handler)
# use the opener to fetch a URL
response = opener.open('http://192.168.1.1')
print(response.read().decode('gbk'))    #为啥路由器网页要用GBK编码呢
# Install the opener.
# Now all calls to urllib2.urlopen use our opener.
#urllib2.install_opener(opener)
测试后返回：

<noframes><body>对不起，您的浏览器不支持框架！</body></noframes>
</HTML>
容我回想一下怎么伪装浏览器@bilibiliuser.spacename

import urllib.request
# create a password manager
password_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()
#伪装浏览器
target = 'http://192.168.1.1'
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windos NT)'
headers = {'User-Agent': user_agent}
req = urllib.request.Request(target, headers=headers)
# Add the username and password.
username = 'admin'  #家里路由器的默认用户名密码
password = 'admin'
# If we knew the realm, we could use it instead of ``None``.
top_level_url = "http://192.168.1.1"
password_mgr.add_password(None, top_level_url, username, password)
handler = urllib.request.HTTPBasicAuthHandler(password_mgr)
# create "opener" (OpenerDirector instance)
opener = urllib.request.build_opener(handler)
# use the opener to fetch a URL
response = opener.open(req)
print(response.read().decode('gbk'))
# Install the opener.
# Now all calls to urllib2.urlopen use our opener.
#urllib2.install_opener(opener)
 
我尽力了 
然而并没有什么卵用*sigh* 
还是框架不支持 
需要进一步学习

- 一点疑问

如果我想用多个handler，能把他们造成一个opener吗？
In the above example we only supplied our HHTPBasicAuthHandler to build_opener. By default openers have the handlers for normal situations - ProxyHandler, UnknownHandler, HTTPHandler, HTTPDefaultErrorHandler, HTTPRedirectHandler, FTPHandler, FileHandler, HTTPErrorProcessor.
+
@drliunt 2015-09-23 23:13 字数 阅读 0