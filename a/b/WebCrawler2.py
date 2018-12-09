import urllib.request as urlrequest
from bs4 import BeautifulSoup

UrL = 'https://movie.douban.com/subject/26387939/'
header={"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36"}
httpproxy_handler = urlrequest.ProxyHandler({"https" : "180.104.107.46"})
opener = urlrequest.build_opener(httpproxy_handler)
web_pages = opener.open(UrL).read()

soup = BeautifulSoup(web_pages,'lxml')
print(soup.find(class_ = 'll rating_num').get_text())

