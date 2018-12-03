from bs4 import BeautifulSoup
import urllib.request as urlrequest
import io
import sys

# 获取html
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')
url_visit = 'http://www.weather.com.cn/textFC/hb.shtml'
crawl_contect = urlrequest.urlopen(url_visit).read()
# print(crawl_contect.decode('unicode-escape'))


# 整理
soup = BeautifulSoup(crawl_contect,'lxml')
# print(soup.prettify())
print(soup.find(class_ = 'conMidtab').get_text())
 