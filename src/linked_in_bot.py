import pyautogui as py
from time import sleep
from os import chdir
import random

class Bot():
    def __init__(self):
        self.caminho = "D:/py/LINKEDIN_BOT/src/imgs"
        chdir(self.caminho)

        self.img_like = "img_like.png"
        self.img_seguir = "img_seguir.png"
        self.img_att_feed = "att_feed.png"
        self.img_conectar = "img_conectar.png"
        self.img_participe = "img_participe.png"
        self.minha_rede = "img_minha_rede.png"
        self.att_feed = "att_feed.png"

        self.random = random.randint(1,3)


    def like(self):
        sleep(self.random)
        try:
            like = py.locateCenterOnScreen(self.img_like, confidence=0.8)
            if like is not None:
                py.moveTo(like, duration=0.2)
                py.click()
            else:
                py.press("pagedown")
        except:
            pass

    def seguir(self):
        sleep(self.random)
        try:
            seguir = py.locateCenterOnScreen(self.img_seguir, confidence=0.8)
            if seguir is not None:
                py.moveTo(seguir, duration=0.2)
                py.click()
            else:
                py.press("pagedown")
        except:
            pass

    def coenctar(self):
        sleep(3)
        try:
            conectar = py.locateCenterOnScreen(self.img_conectar, confidencete=0.8)
            if conectar is not None:
                py.moveTo(conectar, duration=0.2)
                py.click()
            else:
                py.press("pagedown")
        except:
            pass
    
    def participe(self):
        sleep(self.random)
        try:
            participe = py.locateOnScreen(self.img_participe, confidence=0.8)
            if participe is not None:
                py.moveTo(participe, duration=0.8)
                py.click()
            else:
                py.press("pagedown")
        except:
            pass
    
    def encminha_rede(self):
        sleep(self.random)
        try:
            minha_rede = py.locateCenterOnScreen(self.minha_rede, confidence=0.8)
            if minha_rede is not None:
                py.moveTo(minha_rede, duration=0.2)
                py.click()
                sleep(10)
            
            else:
                pass
        except:
            pass
    
    def catt_feed(self):
        sleep(self.random)
        try:
            att_feed = py.locateCenterOnScreen(self.img_att_feed, confidence=0.8)
            if att_feed is not None:
                py.moveTo(att_feed, duration=0.8)
                py.click()
                sleep(10)
            
            else:
                pass
        except:
            pass


if __name__ == "__main__":
    bot = Bot()
    bot.seguir()