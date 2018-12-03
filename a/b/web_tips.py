import urllib.request as urlrequest
import io
import sys

# 获取json
# https://blog.csdn.net/bo_mask/article/details/76067790
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')
url_visit = 'http://api.douban.com/v2/movie/top250?start=25&count=25'
crawl_contect = urlrequest.urlopen(url_visit).read()
print(crawl_contect.decode('unicode-escape'))
# crawl_contect = urlrequest.urlopen(url_visit)
# print(crawl_contect.status)
# print(crawl_contect.read.decode('unicode-escape'))


# 获取值
import json
json_contect = json.loads(crawl_contect.decode('utf8'))
print(json_contect['rating']['average'])


# 保存到文件
id = 26387939
rank = json_contect['rating']['average']
with open('douban_movie_rank.txt','a') as outputfile:
    outputfile.write('{} {}'.format(id,rank))




