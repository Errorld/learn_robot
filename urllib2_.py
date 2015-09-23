import urllib.request
response = urllib.request.urlopen('http://www.baidu.com')
html = response.read()
print(html.decode('utf-8'))
input('response=')
print(response)
