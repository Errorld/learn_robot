import urllib.request
# create a password manager
password_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()

#伪装浏览器
target = 'http://192.168.1.1'
user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.125 Safari/537.36'
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
