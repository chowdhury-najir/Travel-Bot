from bs4 import BeautifulSoup
from dateutil.parser import parse
import csv

def getPostLink(posts):
    count=0
    file= open("links.csv",'w')
    writer=csv.writer(file)
    writer.writerow(["post_link"])
    for post in posts:
        # div that contains the posts 
        #content_area=post.find('div')
        #post_txt=content_area.find_all('p')[0:].text
        #finding post link
        link_area=post.find('a',class_='_5msj')
        link=link_area.get('href').split('?')[0]
        writer.writerow([link])
        #print(link)
        #post_id=link.split('/')[-2]
        count+=1
        print("{} posts link collected".format(count))
    print("toatal = {} posts collected".format(count))

