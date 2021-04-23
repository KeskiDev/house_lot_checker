import requests
import time
from bs4 import BeautifulSoup
from bs4 import SoupStrainer
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

unavailabe_color = "#a0a0a0"
haven_color = "cdcdcd"
discord_webhook_url = "discord web hook here"
check_number = 1
notified_lots = []

while True:
    try:
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--incognito')
        options.add_argument('--headless')
        driver = webdriver.Chrome(executable_path='chrome drive location here', chrome_options=options)

        driver.get("lot map website")
        page_source = driver.page_source

        soup = BeautifulSoup(page_source,'html.parser')

        lots_to_keep_an_eye_on = [904,903,909,910,911,912,913,914,916,917,918,920,921,928,929,930,931,932,933,934,935,936,937,938,939,940,941]

        for lot_number in lots_to_keep_an_eye_on:
            lot_and_number = "Lot_{}".format(lot_number)
            lot_in_question = soup.find("polygon", id=lot_and_number)
            if(lot_in_question == None):
                lot_in_question = soup.find("path", id=lot_and_number)

            if(lot_in_question['fill'] != None):
                current_color = lot_in_question['fill']

            if(current_color != unavailabe_color and notified_lots.IndexOf(lot_and_number) == -1):
                #discord
                if(current_color == haven_color):
                    Message = {
                        "content": "There are houses available!!"
                    }

                    requests.post(discord_webhook_url, data=Message)

                notified_lots.append(lot_and_number)

        print(len(notified_lots))
        print(check_number)
        check_number += 1
        time.sleep(25)
    except:
        Message = {
            "content": "Something went wrong"
        }

        requests.post(discord_webhook_url, data=Message)