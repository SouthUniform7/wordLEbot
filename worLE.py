from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
import time

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

browser = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))

browser.get('https://www.nytimes.com/games/wordle/index.html')

time.sleep(5)

#xButton = browser.find_element(By.XPATH, '/html/body/div/div[3]/div/div/svg')

#xButton.click()

#time.sleep(15)

action = ActionChains(browser)

action.send_keys("shits")



#time.sleep(100) #has to sleep or else it will try to find customer buttons before site loads 

def solve(num): 

    #html/body/whole site/board container/whole board/single row/single letter box

    butt = browser.find_element()

    butt.click()
    time.sleep(1)

    endpts = browser.find_element(By.XPATH, '')
    endpts.click()
    time.sleep(1)

    pencil = browser.find_element(By.XPATH, '')
    pencil.click()
    #time.sleep(2)

    select = Select(browser.find_element(By.NAME, ''))
    #time.sleep(2)
    select.select_by_visible_text('')
    #time.sleep(2)

    save = browser.find_element(By.XPATH, '')
    save.click()

    #time.sleep(2)


    #for each page of customers


def script():
    
    #path only needed to check letter correctness

    #html/body/whole site/board container/whole board/single row/single letter box

    xbase = '/html/body/div/div[1]/div/div[row]'
    
    rowpath = By.XPATH('/html/body/div/div[1]/div/div[]')

    for row in range(1,7):   
        rowpathstring = xbase.replace('row', row)

        rowpath = By.XPATH(rowpathstring)

        letterstring = ''

        letterbox = By.XPATH()







        # if (page == 28):
        #     for i in range(1, 7):
        #         settingChange(i)
        #         time.sleep(2)
        #         browser.get('')
        #         time.sleep(3)
        #         for b in range (page-1): 
                    
        #             browser.find_element(By.LINK_TEXT, '').click()
                    
        #     page += 1

        # else:
            
        #     i = 1
        #     while i < 11:
        #         settingChange(i)
        #         browser.get('')
        #         time.sleep(2)
        
        #         for b in range (page-1): 
        #             browser.find_element(By.LINK_TEXT, '').click()
                    
        #         i += 1

        #     page +=1
        #     browser.find_element(By.LINK_TEXT, '').click()
        #     time.sleep(2)

#script()