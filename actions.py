import pyautogui as py
from time import sleep
import os

class Actionslk():
    def __init__(self):
        self.caminho = 'C:\\Users\Documentos\\Desktop\\LINKEDIN_BOT\\images'
        os.chdir(self.caminho)

        self.img_like = 'like.png'
        self.img_seguir = 'seguir.png'
        self.img_conexoes = 'conexoes.png'
        self.img_participe = 'participe.png'
        self.img_resultado = 'resultado.png'
        self.largura, self.altura = py.size()
        self.centro_x = self.largura//2
        self.centro_y = self.altura//2

    def linkelike(self):
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
        sleep(1)
            
    def seguir(self):
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
        sleep(1)

    def like_seguir(self):
        while True:
            self.linkelike()
            sleep(1)
            self.seguir()

    def ap_like(self):
        while True:
            self.linkelike()
    
    def ap_seguir(self):
        while True:
            self.seguir()

    def conexoes(self):
        try:
            mark_conexoes = py.locateCenterOnScreen(self.img_conexoes, confidence=0.8)
            result = py.locateCenterOnScreen(self.img_resultado, confidence=0.8)

            if result is not None:
                py.moveTo(result)
                py.click()
                py.moveTo(self.centro_x, self.centro_y)

            if mark_conexoes is not None:
                py.moveTo(mark_conexoes)
                py.click()
            else:
                print('imagem nao encontrada!!')
                py.press('pagedown')
            sleep(1)
        except Exception as e:
            print(f'error: {e}')

                

    def participe(self):
        try:
            mark_participe = py.locateCenterOnScreen(self.img_participe, confidence=0.8)
            result = py.locateCenterOnScreen(self.img_resultado, confidence=0.8)

            if result is not None:
                py.moveTo(result)
                py.click()
                py.moveTo(self.centro_x, self.centro_y)

            if mark_participe:
                py.moveTo(mark_participe)
                py.click()
            else:
                print('imagem nao encontrada!!')
                py.press('pagedown')
            sleep(1)
        except Exception as e:
            print(f'error{e}')

    def conexoes_participacoes(self):
        while True:
            self.conexoes()
            sleep(1)
            self.participe()

    def ap_conexoes(self):
        while True:
            self.conexoes()

    def ap_participe(self):
        while True:
            self.participe()

    

