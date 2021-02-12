from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import re
from datetime import datetime
import os
import csv
import time
from dateutil.parser import parse
from fileWriter import writeFile
from getPostLink import getPostLink

uname=""
passw=""

url = "https://m.facebook.com/groups/tob.help/"


# Creating a webdriver instance
driver = webdriver.Firefox()

 # Opening facebook homepage
driver.get("https://m.facebook.com")

# Identifying email and password textboxes
email = driver.find_element_by_name("email")
passwd = driver.find_element_by_name("pass")

# Sending user_name and password to corresponding textboxes
email.send_keys(uname)
passwd.send_keys(passw)

# Sending a signal that RETURN key has been pressed
passwd.send_keys(Keys.RETURN)
time.sleep(4)

#bypassing login with picture page
#driver.find_element_by_class_name('_54k8').click()

#getting the fb group homepage
driver.get(url)

time.sleep(4)
#specify the number of scroll down to the page you want
for j in range(0,1000):
    #scrolling down to the page
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    #sleep for 2 seconds before another scroll request
    time.sleep(1)

# get the group's homepage source code
page_text = (driver.page_source)
soup = BeautifulSoup(page_text,'lxml')
posts=soup.find_all('div',class_="_5rgt")
links=getPostLink(posts)

"""
#writing links in a csv file
writer,file = writeFile("links.csv",["postlinks"])
for link in links:
    writer.writerow(links)
file.close()
"""

"""
#write to csv file
file= open("posts.csv",'w')
file_writer=csv.writer(file)
file_writer.writerow(['post_id','posts','comments','date'])
"""

def extractPost(link):
    try:
        driver.get(link)
        page_text = (driver.page_source)
        soup = BeautifulSoup(page_text,'lxml')
        content_body=soup.find('div',class_='story_body_container')
        
        # div that contains the posts 
        post=content_body.find('div',class_="_5rgt")
        content_area=post.find('span',class_='_1-sk')
        if content_area :
            post_txt=content_area.text
        else :
            post_txt=post.div.text        
        #post time 
        post_time=content_body.find('div',class_='_52jc').a.abbr.text
        post_id=link.split('/')[-2]
        print("post:\n {}".format(post_txt))

        #comment section
        

        comment_area=soup.find_all('div',class_="_2a_i")
        comments=[]
        if comment_area:
            print("comments : ")
            for comment in comment_area :
                comment=comment.find('div',class_='_2b06').text
                comments.append(comment)
            print("\n")
        else:
            print("comment area not found")

            
       
        print('\n')
        #print(post_txt,post_time,link)
        #print(post_txt,"\n",post_time)
        file_writer.writerow([post_id,post_txt,comments,post_time])
    except :
        pass

#for link in links :
    #extractPost(link)
        
driver.close()