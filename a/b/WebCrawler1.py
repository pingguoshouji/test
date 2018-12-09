from bs4 import BeautifulSoup
import urllib.request as urlrequest
import io
import sys

# 获取html
# urlopen返回一个类文件对象
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')
url_visit = 'http://forecast.weather.gov/MapClick.php?lat=37.77492773500046&lon=-122.41941932299972#.WUnSFhN95E4'
crawl_contect = urlrequest.urlopen(url_visit).read()
# print(crawl_contect.decode('unicode-escape'))


# 整理
soup = BeautifulSoup(crawl_contect,'lxml')
# print(soup.prettify())
print(soup.find(id='seven-day-forecast-container').get_text())
# soup_forecast=soup.find(id='seven-day-forecast-container')
# date_list=soup_forecast.find_all(class_='period-name')
# desc_list=soup_forecast.find_all(class_='short-desc')
# temp_list=soup_forecast.find_all(class_='temp')
# for i in range(9):
#     date=date_list[i].get_text()
#     desc=desc_list[i].get_text()
#     temp=temp_list[i].get_text()
#     print("{}{}{}".format(date,desc,temp))

 