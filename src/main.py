import linked_in_bot
from time import sleep
import pyautogui as py
import random

class Start():
    def __init__(self):
        self.bot = linked_in_bot.Bot()
        self.random = random.randint(1,2)

    def menu(self):
        print("========== Menu ==========")
        print("Digite 1 para Likes")
        print("Digite 2 para Seguir")
        print("Digite 3 para Seguir e Dar Likes")
        print("Digite 4 para Conexões")
        print("Digite 5 para Participações")
        print("Digite 6 para Participações e Conexões")
        print("==========================")


    def main(self):
        self.menu()
        pergunta = int(input("faça sua escolha (lembrem-se de o programa aceita apenas esses numeros.):  "))
        if pergunta == 1:
            sleep(3)
            print("Você escolheu Likes.")
            while True:
                sleep(self.random)
                self.bot.like()
       
                
        elif pergunta == 2:
            sleep(3)
            print("Você escolheu Seguir.")
            while True:
                sleep(self.random)
                self.bot.seguir()
      
        elif pergunta == 3:
            sleep(3)
            print("Você escolheu Seguir e Dar Likes.")
            while True:
                sleep(self.random)
                self.bot.like()
                self.bot.seguir()

        elif pergunta == 4:
            sleep(3)
            print("Você escolheu Conexões.")
            try:
                self.bot.encminha_rede()
            except:
                print("aconteceu algo inesperado! tente novamente: ")
                self.main()

            while True:
                sleep(self.random)
                self.bot.coenctar()

        elif pergunta == 5:
            sleep(3)
            print("Você escolheu Participações.")
            try:
                self.bot.encminha_rede()
            except:
                print("aconteceu algo inesperado! tente novamente: ")
                self.main()
            while True:
                sleep(self.random)
                self.bot.participe()


        elif pergunta == 6:
            sleep(3)
            print("Você escolheu Participações e Conexões.")
            try:
                self.bot.encminha_rede()
            except:
                print("aconteceu algo inesperado! tente novamente: ")
                self.main()
            
            while True:
                sleep(self.random)
                self.bot.coenctar()
                self.bot.participe()

        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")



if __name__ == "__main__":
    start = Start()
    start.main()