import pyautogui as py
from time import sleep
from os import chdir


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




    def like(self):

        try:
            like = py.locateCenterOnScreen(self.img_like, confidence=0.8)
            if like is not None:
                py.moveTo(like, duration=0.2)
                py.click()
            else:
                self.catt_feed()
                py.press("pagedown")
        except Exception as ex:
            print(f"aconteceu algo inesperado {ex}")

    def seguir(self):
        try:
            seguir = py.locateCenterOnScreen(self.img_seguir, confidence=0.8)
            if seguir is not None:
                py.moveTo(seguir, duration=0.2)
                py.click()
            else:
                self.catt_feed()
                py.press("pagedown")

        except Exception as ex:
            print(f"aconteceu algo inesperado {ex}")

    def coenctar(self):
        try:
            conectar = py.locateCenterOnScreen(self.img_conectar, confidence=0.8)
            if conectar is not None:
                py.moveTo(conectar, duration=0.2)
                py.click()
            else:
                py.press("pagedown")
        except Exception as ex:
            print(f"aconteceu algo inesperado {ex}")
    
    def participe(self):
        try:
            participe = py.locateOnScreen(self.img_participe, confidence=0.8)
            if participe is not None:
                py.moveTo(participe, duration=0.8)
                py.click()
            else:
                py.press("pagedown")
        except Exception as ex:
            print(f"aconteceu algo inesperado {ex}")
    
    def encminha_rede(self):
        try:
            minha_rede = py.locateCenterOnScreen(self.minha_rede, confidence=0.8)
            if minha_rede is not None:
                py.moveTo(minha_rede, duration=0.2)
                py.click()
                sleep(10)
            
            else:
                print("error")
        except Exception as ex:
            print(f"aconteceu algo inesperado {ex}")
    
    def catt_feed(self):
        try:
            att_feed = py.locateCenterOnScreen(self.img_att_feed, confidence=0.8)
            if att_feed is not None:
                py.moveTo(att_feed, duration=0.8)
                py.click()
                sleep(10)
            
            else:
                pass
        except Exception as ex:
            print(f"aconteceu algo inesperado {ex}")