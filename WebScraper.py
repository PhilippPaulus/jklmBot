from typing import Optional
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

JKML_PATH = "https://jklm.fun/"

class WebScraper:
    def __init__(self) -> None:
        chrome_options = Options()
        chrome_options.add_argument("--no-first-run")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-metrics")
        chrome_options.add_argument("--disable-translate")
        chrome_options.add_argument("--bwsi")
        chrome_options.add_argument("--disable-search-engine-choice-screen")

        self.browser = webdriver.Chrome(options = chrome_options)
        self.browser.get(JKML_PATH)

    def getUrl(self) -> str:
        return self.browser.current_url        
    
    def readCode(self) -> Optional[str]:
        try:
            gameElem = self.browser.find_element(By.CLASS_NAME, "game")
            iFrame = gameElem.find_element(By.TAG_NAME, "iframe")
            
            self.browser.switch_to.frame(iFrame)

            pattern = self.browser.find_element(By.CLASS_NAME, "syllable").text

            self.browser.switch_to.default_content()

            return pattern

        except NoSuchElementException:
            return None
    
    def inputWord(self, word: str) -> None:
        try:
            gameElem = self.browser.find_element(By.CLASS_NAME, "game")
            iFrame = gameElem.find_element(By.TAG_NAME, "iframe") 
            self.browser.switch_to.frame(iFrame)


            elem = self.browser.find_element(By.CLASS_NAME, "selfTurn")
            inputField = elem.find_element(By.TAG_NAME, "input")


            inputField.send_keys(word)
            time.sleep(0.05)
            inputField.send_keys(Keys.RETURN)


            self.browser.switch_to.default_content()
        
        except:
            self.browser.switch_to.default_content()
        
    def isMyTurn(self) -> bool:  
        try:
            gameElem = self.browser.find_element(By.CLASS_NAME, "game")
            iFrame = gameElem.find_element(By.TAG_NAME, "iframe")
            
            self.browser.switch_to.frame(iFrame)

            elem = self.browser.find_element(By.CLASS_NAME, "selfTurn")

            if elem.is_displayed():
                self.browser.switch_to.default_content()
                return True
            
            self.browser.switch_to.default_content()
            return False
        
        except:
            return False
        

