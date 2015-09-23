import urllib
import urllib.request

url = 'http://www.someserver.com/register.cgi'

values = {'name': 'WHY', 'location': 'SDU', 'language': 'python' }
data = urllib.parse.urlencode(values)
req = urllib.request.Request(url, data)
response = urllib.request.urlopen(req)
the_page = response.read()