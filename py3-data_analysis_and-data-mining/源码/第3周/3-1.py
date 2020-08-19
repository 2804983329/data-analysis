'''
import urllib.request
import re
url="http://blog.csdn.net/"
headers=("User-Agent","Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.22 Safari/537.36 SE 2.X MetaSr 1.0")
opener=urllib.request.build_opener()
opener.addheaders=[headers]
urllib.request.install_opener(opener)
data=urllib.request.urlopen(url).read().decode("utf-8","ignore")
pat='<h3  class="tracking-ad" data-mod="popu_254"><a href="(.*?)"'
result=re.compile(pat).findall(data)
for i in range(0,len(result)):
    file="F:/天善-Python数据分析与挖掘课程/result/31/"+str(i)+".html"
    urllib.request.urlretrieve(result[i],filename=file)
    print("第"+str(i+1)+"次爬取成功")
'''

'''
import urllib.request
def use_proxy(url,proxy_addr):
    proxy=urllib.request.ProxyHandler({"http":proxy_addr})
    opener=urllib.request.build_opener(proxy,urllib.request.HTTPHandler)
    urllib.request.install_opener(opener)
    data=urllib.request.urlopen(url).read().decode("utf-8","ignore")
    return data
proxy_addr=["119.183.220.224:8888",""]
url="http://www.baidu.com"
data=use_proxy(url,proxy_addr)
print(len(data))
'''

import urllib.request
import re
keyname="连衣裙"
key=urllib.request.quote(keyname)
headers=("User-Agent","Mozilla/5.0 (Windows NT 6.1; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0")
opener=urllib.request.build_opener()
opener.addheaders=[headers]
urllib.request.install_opener(opener)
for i in range(1,101):
    url="https://s.taobao.com/list?q="+key+"&cat=16&style=grid&seller_type=taobao&spm=a219r.lm874.1000187.1&bcoffset=12&s="+str(i*60)
    data=urllib.request.urlopen(url).read().decode("utf-8","ignore")
    pat='pic_url":"//(.*?)"'
    imagelist=re.compile(pat).findall(data)
    for j in range(0,len(imagelist)):
        thisimg=imagelist[j]
        thisimgurl="http://"+thisimg
        file="F:/天善-Python数据分析与挖掘课程/result/31/img/"+str(i)+str(j)+".jpg"
        urllib.request.urlretrieve(thisimgurl,filename=file)

