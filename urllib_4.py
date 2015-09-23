import urllib.request    
import urllib  
data = {}  
data['wd'] = 'WHY'    
data['ie'] = 'utf-8'
url_values = urllib.parse.urlencode(data)    
print(url_values)  #ie=utf-8&wd=WHY
url = 'http://www.baidu.com/s'    
full_url = url + '?' + url_values  
print(full_url)	#http://www.baidu.com/s?ie=utf-8&wd=WHY
data = urllib.request.urlopen(full_url)   
print(data.read().decode('utf-8'))