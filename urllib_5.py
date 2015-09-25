import urllib.request
myUrl = 'http://www.qiushibaike.com'
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2504.0 Safari/537.36'
headers = { 'User-Agent' : user_agent }
req = urllib.request.Request(myUrl, headers = headers)
try:
	response = urllib.request.urlopen(req)
	print(response.read().decode('utf8','ignore'))
	print('succed')
except urllib.request.URLError as e:
	#print(dir(e))
	print(e.code)