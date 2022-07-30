from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

browser = webdriver.Chrome(ChromeDriverManager().install())


time.sleep(5) #has to sleep or else it will try to find customer buttons before site loads 

def settingChange(num): 

    xpth = asdf

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



page = 28

#for each page of customers
while page < 29:

    
    if (page == 28):
        for i in range(1, 7):
            settingChange(i)
            time.sleep(2)
            browser.get('')
            time.sleep(3)
            for b in range (page-1): 
                
                browser.find_element(By.LINK_TEXT, '').click()
                
        page += 1

    else:
        
        i = 1
        while i < 11:
            settingChange(i)
            browser.get('')
            time.sleep(2)
    
            for b in range (page-1): 
                browser.find_element(By.LINK_TEXT, '').click()
                
            i += 1

        page +=1
        browser.find_element(By.LINK_TEXT, '').click()
        time.sleep(2)