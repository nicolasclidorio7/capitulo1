class Menu:  
    def iniciar_jogo(self):  
        print("O jogo começou!")  

    def mostrar_opcoes(self):  
        print("1. Iniciar Jogo")  
        print("2. Configurações")  
        print("3. Sair")  

    def sair(self):  
        print("Saindo do jogo. Até logo!")  

# Instanciando a classe  
meu_menu = Menu()  

# Testando os métodos  
meu_menu.iniciar_jogo()  
meu_menu.mostrar_opcoes()  
meu_menu.sair()  
