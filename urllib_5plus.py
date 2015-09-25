import urllib.request

req = urllib.request.Request('http://www.qiushibaike.com/8hr/page/1')
try:
	urllib.request.urlopen(req)
	print('succed')
except urllib.request.URLError as e:
	#print(dir(e))
	print(e.code)