from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
browser = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))


###########################################################
#   GGGGG   L        OOOO    BBBB      AAA   L
#   G        L       O    O   B   B     A  A   L
#   G        L       O    O   BBBBB    A   A   L
#   G  GG    L       O    O   B    B   AAAAA   L
#   G   G    L       O    O   B    B   A    A   L
#   GGGGG   LLLLLL  OOOO    BBBBB   A     A   LLLLLL
###########################################################
letters = ['s', 't', 'r', 'a', 'y']

xbase = '/html/body/div/div[1]/div/div[row]'

###########################################################


def send_word(word):

    ActionChains(browser) \
        .send_keys(word) \
        .key_down(Keys.ENTER) \
        .key_up(Keys.ENTER) \
        .perform()
    time.sleep(2)

    return

def solve(row = 1): 

    if (row > 6):
        print('bruh')
    else:
    
        #rowpath = By.XPATH(xbase.replace('row', str(row)))

        word_string = ""


        #because for some reason python string .join(letters) was returning blank
        for i in letters: 
            word_string += i

        print(word_string)
        send_word(word_string)
        
        row+=1

        solve(row)
        
    


def script():
    
    #path only needed to check letter correctness

    #html/body/whole site/board container/whole board/single row/single letter box

    browser.get('https://www.nytimes.com/games/wordle/index.html')

    time.sleep(1)

    xButton = browser.find_element(By.XPATH, '/html/body/div/div[3]/div/div')

    xButton.click()

    time.sleep(1)

    solve()

script()