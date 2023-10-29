from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys



class Linkedin():
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.site_link = 'https://br.linkedin.com'
        self.site_map = {
            'XP':{
                'login': '/html/body/main/section[1]/div/div/form/div[1]/div[1]/div/div/input',
                'senha': '/html/body/main/section[1]/div/div/form/div[1]/div[2]/div/div/input',
                'entra': '/html/body/main/section[1]/div/div/form/div[2]/button',
            }
        }
        self.login = input('digite seu e-mail:  ')
        self.senha = input('digite sua senha:  ')

    def main(self):
        self.abre()
        sleep(5)
        self.loga()
        sleep(5)

    def abre(self):
        self.driver.get(self.site_link)
        self.driver.maximize_window()

    def loga(self):
        try:
            id = self.driver.find_element(By.XPATH, self.site_map['XP']['login'])
            password = self.driver.find_element(By.XPATH, self.site_map['XP']['senha'])
            entra = self.driver.find_element(By.XPATH, self.site_map['XP']['entra'])

            if id and password and entra:
                id.send_keys(self.login)
                sleep(1)
                password.send_keys(self.senha)
                sleep(1)
                entra.click()

        except NoSuchElementException:
            print('elemento nao encontrado. tentando novamente...')
            try:
                self.loga()   
            except NoSuchElementException:
                print('elemento nao encontrado, abra o programa novamente')
                sleep(1.5)
                exit()

        except Exception as e:
            print(f'error: {e}')
