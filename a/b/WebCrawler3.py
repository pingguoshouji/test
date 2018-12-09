import urllib.request as urlrequest
import time
import random

IMG_PATH = './imgs/{}.jpg'
DATA_FILE = './data/votes.csv'
STORED_IMG_ID_FILE = './data/cached_img.txt'
STORED_IMG_IDS = set()
IMG_URL = 'https://maps.googleapis.com/maps/api/streetview?size=400x300&location={},{}'

IMG_PATH = './imgs/{}.jpg'
DATA_FILE = './data/votes.csv'
STORED_IMG_ID_FILE = './data/cached_img.txt'
STORED_IMG_IDS = set()
IMG_URL = 'https://maps.googleapis.com/maps/api/streetview?size=400x300&location={},{}'

with open(STORED_IMG_ID_FILE) as input_file:
    for line in input_file:
        STORED_IMG_IDS.add(line.strip())

with open(DATA_FILE) as input_file:
    skip_first_line = True
    for line in input_file:
        if skip_first_line:
            skip_first_line = False
            continue
        left_id, right_id, winner, left_lat, left_long, right_lat, right_long, category = line.split(',')

        if left_id not in STORED_IMG_IDS:
            print ('saving img {}...'.format(left_id))
            urlrequest.urlretrieve(IMG_URL.format(left_lat, left_long), IMG_PATH.format(left_id))
            STORED_IMG_IDS.add(left_id)
            with open(STORED_IMG_ID_FILE, 'a') as output_file:
                output_file.write('{}\n'.format(left_id))
            time.sleep(1)  # wait some time, trying to avoid google forbidden (of crawler)

        if right_id not in STORED_IMG_IDS:
            print ('saving img {}...'.format(right_id))
            urlrequest.urlretrieve(IMG_URL.format(right_lat, right_long), IMG_PATH.format(right_id))
            STORED_IMG_IDS.add(right_id)
            with open(STORED_IMG_ID_FILE, 'a') as output_file:
                output_file.write('{}\n'.format(right_id))
            time.sleep(1)  # wait some time, trying to avoid google forbidden (of crawler)


import urllib
from urllib import request

# head = {'User-Agent':"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)"}
hander = urllib.request.HTTPHandler() 
opener = urllib.request.build_opener(hander)
request = urllib.request.Request("http://www.baidu.com/")
request.add_header('User-Agent',"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)")
response = opener.open(request).read()
print(response)
