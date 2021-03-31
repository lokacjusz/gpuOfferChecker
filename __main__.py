import time
import requests
import popup_tray
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys

url = "https://www.pepper.pl/grupa/karty-graficzne"
###########
###########
#print(ids[0])
###########
###########
###
#last_offer_id = soup.find(id=['thread_377725'])
#print(last_offer_id)
###

##list all tags
#print([tag.name for tag in soup.find_all()])
##
i=0
while(True):
    i=i+1
    print("check no. {0}".format(i))
    try:
        html_doc = requests.get(url)
        soup = BeautifulSoup(html_doc.text,'html.parser')
        ids = [tag['id'] for tag in soup.select('article[id]')]
        img = soup.find_all('img')
        GPU_name = (img[1].get('alt'))
        with open('X:\\python\\pepper_gpu_checker\\id.txt', 'a+') as file:
            file.seek(0) ##set cursor on zero char - at the very first char
            data = file.read().replace('\n', '')
            #print("data: {0}".format(data))
            #file.write(ids[0])
            if str(ids[0]).strip() != str(data).strip():
                #print(ids[0])
                new_offer = soup.article.a.get("href")
                print(soup.article.a.get("href"))
                driver = webdriver.Firefox(executable_path="X:\\python\\pepper_gpu_checker\\geckodriver.exe")
                #driver.get(new_offer)
                driver.get(url)
                file.truncate(0)
                file.write(ids[0])
                file.close()
                popup_tray.popup_notification(img[1].get('alt'))
            else:
                print("no updates")
    except:
        print("failure. retry after 5 minutes")
    time.sleep(360)