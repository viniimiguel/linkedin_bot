import linkbot
import actions
from time import sleep

class Bot():
    def __init__(self):
        self.linkedin_instance = linkbot.Linkedin()
        self.actions_instance = actions.Actionslk()
        print("""LINKEBOT  ESCOLHA OQUE VOCE QUER FAZER COM O LINKEBOT: \n [1] APENAS PARA DAR LIKES, [2] PARA SEGUIR E DAR LIKES, [3] PARA APENAS SEGUIR.
              \n[4] PARA CONEXÕES, [5] PARA PARTICIPAR DE GRUPOS, [6] PARA CONEXOES E PARTICIPAÇÕES.             
              """)
        self.definicao = int(input('Qual sua opção?: '))


    def main(self):
        self.use_abrir()
        sleep(5)
        if self.definicao == 1:
            self.use_likes()
            print('iniciando função 1')
        
        elif self.definicao == 2:
            self.use_seguir()
            print('iniciando função 2')

        elif self.definicao == 3:
            self.use_like_seguir()
            print('iniciando função 3')

        elif self.definicao == 4:
            self.use_conexoes()
            print('iniciando função 4')
        
        elif self.definicao == 5:
            self.use_participe()
            print('iniciando função 5')

        elif self.definicao == 6:
            self.use_conexoes_participe()
            print('iniciando função 6')

    def use_abrir(self):
        self.linkedin_instance.main()
    
    def use_likes(self):
        self.actions_instance.ap_like()

    def use_seguir(self):
        self.actions_instance.ap_seguir()
    
    def use_like_seguir(self):
        self.actions_instance.like_seguir()
    
    def use_conexoes(self):
        self.actions_instance.ap_conexoes()

    def use_participe(self):
        self.actions_instance.ap_participe()

    def use_conexoes_participe(self):
        self.actions_instance.conexoes_participacoes()



bot = Bot()
bot.main()

        
