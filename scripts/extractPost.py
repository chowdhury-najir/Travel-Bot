from bs4 import BeautifulSoup
from dateutil.parser import parse
#from main import initDriver



def extractPost(link,driver):
    try:
        print(driver)
        driver.get(link,driver)
        page_text = (driver.page_source)
        soup = BeautifulSoup(page_text,'lxml')
        content_body=soup.find('div',class_='story_body_container')
        print(content_body)
        
        # div that contains the posts 
        post=content_body.find('div',class_="_5rgt")
        content_area=post.find('span',class_='_1-sk')
        if content_area :
            post_txt=content_area.text
        else :
            post_txt=post.div.text

        #post time 
        post_time=content_body.find('div',class_='_52jc').a.abbr.text
            
        print(post_txt)
        #print('\n\n\n')
        print(post_time,"\n",link)
    except :
        pass
print("****************extracting post")

    
    
        