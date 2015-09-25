import urllib.request
req = urllib.request.Request('http://www.baidu.com')    #req这部分应该可以修改request header等内容
response = urllib.request.urlopen(req)  #req 是加了料的('http://www.baidu.com')

the_page = response.read()    
print(the_page)
