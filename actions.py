import pyautogui as py
from time import sleep
import os

class Actionslk():
    def __init__(self):
        self.caminho = 'C:\\Users\Documentos\\Desktop\\LINKEDIN_BOT\\images'
        os.chdir(self.caminho)

        self.img_like = 'like.png'
        self.img_seguir = 'seguir.png'

    def linkelike(self):
        while True:
            try:
                mark_like = py.locateCenterOnScreen(self.img_like, confidence=0.8)
                if mark_like is not None:
                    py.moveTo(mark_like)
                    py.click()
                
                else:
                    print('imagem nao encontrada!!')
                    py.press('pagedown')
                sleep(1)
            except Exception as e:
                print(f'error: {e}')
            
    def seguir(self):
        while True:
            try:
                mark_seguir = py.locateCenterOnScreen(self.img_seguir, confidence=0.8)
                if mark_seguir is not None:
                    py.moveTo(mark_seguir)
                    py.click()
                else:
                    print('imagem nao encontrada!!')
                    py.press('pagedown')
                sleep(1)
            except Exception as e:
                print(f'error: {e}')


actionslk = Actionslk()
actionslk.seguir()
    

