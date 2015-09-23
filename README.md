# 学习网络爬虫

标签（空格分隔）： Python 爬虫 urllib

---

##1. 来源
> [请叫我汪海的CSDN博客](http://blog.csdn.net/pleasecallmewhy/article/details/8923067)

从这里开始学习爬虫
##2. 基本入门()`import urllib.request`
###1. urlopen
```
response = urllib.request.urlopen('http://www.baidu.com/')  
html = response.read()  
print html  
```
urlopen 把request 发给url 并把response 返回
###2. Request
```
import urllib.request
req = urllib.request.Request('http://www.baidu.com')    #req这部分应该可以修改request header等内容
response = urllib.request.urlopen(req)  #req 是加了料的('http://www.baidu.com')
the_page = response.read()    
print(the_page)
```
这段代码和1. rulopen 效果一样。
> 在HTTP请求时，允许你做额外的两件事。
> ####1. 发送data表单数据
这个内容相信做过Web端的都不会陌生，
有时候你希望发送一些数据到URL(通常URL与CGI[通用网关接口]脚本，或其他WEB应用程序挂接)。
在HTTP中,这个经常使用熟知的POST请求发送。
这个通常在你提交一个HTML表单时由你的浏览器来做。
并不是所有的POSTs都来源于表单，你能够使用POST提交任意的数据到你自己的程序。
一般的HTML表单，data需要编码成标准形式。然后做为data参数传到Request对象。
编码工作使用urllib的函数而非urllib2。
我们新建一个文件urllib2_test03.py来感受一下：

```
import urllib
import urllib.request
url = 'http://www.someserver.com/register.cgi'
values = {'name': 'WHY', 'location': 'SDU', 'language': 'python' }
data = urllib.parse.urlencode(values)   #urllib.urlencode在python3
req = urllib.request.Request(url, data)
response = urllib.request.urlopen(req)
the_page = response.read()
```
```
>>> import urllib.request
>>> test = urllib.parse.urlencode(di)   #urlencode在urllib.request中
>>> print(test)
ff=ffff&dfdsaf=fasdf    #编码成header形式
```

> 通过fiddler查看header
![](http://7xlyu9.com1.z0.glb.clouddn.com/15-9-23/67467394.jpg)
![](http://7xlyu9.com1.z0.glb.clouddn.com/15-9-23/58314171.jpg)

> 如果没有传送data参数，urllib2使用GET方式的请求。
GET和POST请求的不同之处是POST请求通常有"副作用"，
它们会由于某种途径改变系统状态(例如提交成堆垃圾到你的门口)。
Data同样可以通过在Get请求的URL本身上面编码来传送。

```
import urllib.request    
import urllib  
data = {}  
data['wd'] = 'WHY'    
data['ie'] = 'utf-8'
url_values = urllib.parse.urlencode(data)    
print(url_values)  #ie=utf-8&wd=WHY
url = 'http://www.baidu.com/s'    
full_url = url + '?' + url_values  
print(full_url) #http://www.baidu.com/s?ie=utf-8&wd=WHY
data = urllib.request.urlopen(full_url)   
#print(data.read().decode('utf-8')) 
```
搜索了“WHY” via ‘http://www.baidu.com/s?ie=utf-8&wd=WHY’(只要wd一个字串也可以)
**这是GET`urlopen(arg)`**
![](http://7xlyu9.com1.z0.glb.clouddn.com/15-9-23/90523066.jpg)

##3. 伪装浏览器
```
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windos NT)'
#urllib.request.urlencode(user_agent)
headers = {'User-Agent': user_agent}	
req = urllib.request.Request(url, headers=headers)  
response = urllib.request.urlopen(req)
```
- 注意[headers=headers](http://stackoverflow.com/questions/22403871/content-length-should-be-specified-for-iterable-data-of-type-class-dict)

##- 问题与解决问题

1. python3 中urllib2 由urllib.request 替代
2. urllib.request.openurl('url').read() 是BYTES信息，一般是UTF8编码。如果直接print 会显示/x**/x**/x** 的UTF8代码。
    - 需要进行`decode('utf-8')`后能输出中文在屏幕上
    - [ ] 但是windows 命令行下又有GBK编码问题，待解决。
3. 为了不再WINDOWS上使用命令行，使用IDLE发现其打开HTML后反应缓慢。
    - [ ] 考虑换IDE
    - [X] 考虑换LINUX




