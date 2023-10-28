from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class Linkedin():
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.site_link = 'https://br.linkedin.com'
        self.site_map = {
            'XP':{
                'login': '/html/body/main/section[1]/div/div/form/div[1]/div[1]/div/div/input',
                'senha': '/html/body/main/section[1]/div/div/form/div[1]/div[2]/div/div/input',
            }
        }

    def main(self):
        self.abre()
        sleep(237819)

    def abre(self):
        self.driver.get(self.site_link)
        self.driver.maximize_window()

    def loga(self):
        login = input('digite seu e-mail:  ')
        senha = input('digite sua senha:  ')

        self.driver.find_element(By.XPATH, self.site_map['XP']['login'])
        self.driver.find_element(By.XPATH, self.site_map['XP']['senha'])



linkedin = Linkedin()
linkedin.main()