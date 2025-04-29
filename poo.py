class Jogo:  
    def iniciar(self):  
        print("O jogo começou!")  

# Instanciando a classe  
meu_jogo = Jogo()  

# Chamando o método iniciar  
meu_jogo.iniciar()  


class Personagem:  
    def pular(self):  
        print("O personagem pulou!")  

# Instanciando a classe  
meu_personagem = Personagem()  

# Chamando o método pular  
meu_personagem.pular()  


class Inimigo:  
    def atacar(self):  
        print("O inimigo atacou!")  

# Instanciando a classe  
meu_inimigo = Inimigo()  

# Chamando o método atacar  
meu_inimigo.atacar()  


class Pontuacao:  
    def zerar_pontos(self):  
        print("Pontuação zerada!")  

# Instanciando a classe  
minha_pontuacao = Pontuacao()  

# Chamando o método zerar_pontos  
minha_pontuacao.zerar_pontos()  


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

class Personagem:  
    def __init__(self, nome):  
        self.nome = nome  

    def dizer_nome(self):  
        print(f"Meu nome é {self.nome}")  

# Instanciando um personagem  
personagem1 = Personagem("Aragorn")  

# Testando o método  
personagem1.dizer_nome()  

class Pontuacao:  
    def __init__(self):  
        self.pontos = 0  # Inicializa os pontos em 0  

    def adicionar_pontos(self, quantidade):  
        self.pontos += quantidade  # Adiciona a quantidade ao total de pontos  

    def mostrar_pontos(self):  
        print(f"Pontuação atual: {self.pontos}")  # Exibe os pontos atuais  

# Exemplo de uso da classe Pontuacao  
pontuacao1 = Pontuacao()  

# Adicionando pontos e mostrando a pontuação  
pontuacao1.adicionar_pontos(10)  
pontuacao1.mostrar_pontos()  # Saída: Pontuação atual: 10  

pontuacao1.adicionar_pontos(5)  
pontuacao1.mostrar_pontos()  # Saída: Pontuação atual: 15  

class Personagem:  
    def __init__(self):  
        self.vida = 100  # Inicializa a vida em 100  

    def tomar_dano(self, dano):  
        self.vida -= dano  # Reduz a vida pelo valor de dano  
        if self.vida <= 0:  
            self.vida = 0  # Garante que a vida não fique negativa  
            print("Game Over!")  # Imprime mensagem de fim de jogo  
        else:  
            print(f"Vida restante: {self.vida}")  # Exibe vida restante  

# Exemplo de uso da classe Personagem  
personagem1 = Personagem()  

# Testando o método tomar_dano  
personagem1.tomar_dano(30)  # Vida restante: 70  
personagem1.tomar_dano(60)  # Vida restante: 10  
personagem1.tomar_dano(15)  # Game Over!  

class Jogador:  
    def __init__(self):  
        self.energia = 50  # Inicializa a energia em 50  

    def recuperar_energia(self, quantidade):  
        self.energia += quantidade  # Aumenta a energia  
        print(f"Energia recuperada! Energia atual: {self.energia}")  

    def usar_energia(self, quantidade):  
        self.energia -= quantidade  # Reduz a energia  
        if self.energia < 0:  
            self.energia = 0  # Garante que a energia não fique negativa  
            print("Sem energia suficiente!")  # Avise se a energia for insuficiente  
        else:  
            print(f"Energia usada. Energia atual: {self.energia}")  

# Exemplo de uso da classe Jogador  
jogador1 = Jogador()  

# Usando e recuperando energia  
jogador1.usar_energia(20)  # Saída: Energia usada. Energia atual: 30  
jogador1.usar_energia(40)  # Saída: Sem energia suficiente!  
jogador1.recuperar_energia(10)  # Saída: Energia recuperada! Energia atual: 10  
jogador1.usar_energia(5)  # Saída: Energia usada. Energia atual: 5  
jogador1.usar_energia(10)  # Saída: Sem energia suficiente!  

class Personagem:  
    def __init__(self):  
        self.vida = 100  # Inicializa a vida em 100  

    def tomar_dano(self, dano):  
        self.vida -= dano  # Reduz a vida pelo valor de dano  
        if self.vida <= 0:  
            self.vida = 0  # Garante que a vida não fique negativa  
            print("Game Over!")  # Imprime mensagem de fim de jogo  
        else:  
            print(f"Vida restante: {self.vida}")  # Exibe vida restante  


class Inimigo:  
    def __init__(self, nome):  
        self.nome = nome  
        self.vida = 100  # Inicializa a vida em 100  

    def atacar(self, alvo):  
        if isinstance(alvo, Personagem):  # Verifica se o alvo é um personagem  
            dano = 10  
            print(f"{self.nome} atacou!")  
            alvo.tomar_dano(dano)  # Reduz a vida do alvo em 10 pontos  
        else:  
            print("O alvo não é um personagem!")  

# Exemplo de uso das classes  
personagem1 = Personagem()  
inimigo1 = Inimigo("Goblin")  

# Inimigo ataca o personagem  
inimigo1.atacar(personagem1)  # Exibe a vida do personagem após o ataque  
inimigo1.atacar(personagem1)  # Ataque adicional  

import random  

class Personagem:  
    def __init__(self, nome):  
        self.nome = nome  
        self.vida = 100  # Inicializa a vida em 100  

    def atacar(self, alvo):  
        dano = random.randint(5, 20)  # Dano aleatório entre 5 e 20  
        print(f"{self.nome} ataca {alvo.nome} e causa {dano} de dano.")  
        alvo.tomar_dano(dano)  

    def tomar_dano(self, dano):  
        self.vida -= dano  # Reduz a vida pelo valor de dano  
        if self.vida <= 0:  
            self.vida = 0  # Garante que a vida não fique negativa  
            print(f"{self.nome} foi derrotado!")  # Imprime mensagem de derrota  
        else:  
            print(f"Vida de {self.nome} restante: {self.vida}")  

class Inimigo:  
    def __init__(self, nome):  
        self.nome = nome  
        self.vida = 100  # Inicializa a vida em 100  

    def atacar(self, alvo):  
        dano = random.randint(5, 20)  # Dano aleatório entre 5 e 20  
        print(f"{self.nome} ataca {alvo.nome} e causa {dano} de dano.")  
        alvo.tomar_dano(dano)  

    def tomar_dano(self, dano):  
        self.vida -= dano  # Reduz a vida pelo valor de dano  
        if self.vida <= 0:  
            self.vida = 0  # Garante que a vida não fique negativa  
            print(f"{self.nome} foi derrotado!")  # Imprime mensagem de derrota  
        else:  
            print(f"Vida de {self.nome} restante: {self.vida}")  

# Função para simular o combate  
def simular_combate(personagem, inimigo):  
    turn = 0  # Controle de turnos  
    while personagem.vida > 0 and inimigo.vida > 0:  
        if turn % 2 == 0:  # Turno do personagem  
            personagem.atacar(inimigo)  
        else:  # Turno do inimigo  
            inimigo.atacar(personagem)  
        turn += 1  # Alterna o turno  

    # Determinando o vencedor  
    if personagem.vida > 0:  
        print(f"{personagem.nome} ganhou a batalha!")  
    else:  
        print(f"{inimigo.nome} ganhou a batalha!")  

# Exemplo de uso da simulação de combate  
if __name__ == "__main__":  
    personagem1 = Personagem("Heroi")  
    inimigo1 = Inimigo("Monstro")  

    simular_combate(personagem1, inimigo1)  

    import random  

class Pontuacao:  
    def __init__(self):  
        self.pontos = 0  # Inicializa a pontuação em 0  

    def adicionar_pontos(self, quantidade):  
        self.pontos += quantidade  # Adiciona pontos  
        print(f"Pontos atuais: {self.pontos}")  # Mostra pontuação atual  


class Inimigo:  
    def __init__(self, nome):  
        self.nome = nome  
        self.vida = 100  # Inicializa a vida em 100  

    def atacar(self, alvo):  
        dano = random.randint(5, 20)  # Dano aleatório entre 5 e 20  
        print(f"{self.nome} ataca {alvo.nome} e causa {dano} de dano.")  
        alvo.tomar_dano(dano)  

    def tomar_dano(self, dano):  
        self.vida -= dano  # Reduz a vida pelo valor de dano  
        if self.vida <= 0:  
            self.vida = 0  # Garante que a vida não fique negativa  
            print(f"{self.nome} foi derrotado!")  # Imprime mensagem de derrota  
        else:  
            print(f"Vida de {self.nome} restante: {self.vida}")  


class Jogador:  
    def __init__(self, nome):  
        self.nome = nome  
        self.energia = 100  # Inicializa a energia em 100  
        self.pontos = Pontuacao()  # Inicializa um objeto de pontuação  

    def atacar(self, alvo):  
        if self.energia <= 0:  
            print(f"{self.nome} está sem energia! É necessário descansar para continuar atacando.")  
            return  

        dano = random.randint(5, 20)  # Dano aleatório entre 5 e 20  
        print(f"{self.nome} ataca {alvo.nome} e causa {dano} de dano.")  
        alvo.tomar_dano(dano)  
        self.energia -= 10  # Perde 10 de energia  
        print(f"Energia de {self.nome} restante: {self.energia}")  

        if alvo.vida <= 0:  
            self.pontos.adicionar_pontos(10)  # Adiciona 10 pontos ao derrotar o inimigo  

    def descansar(self):  
        if self.energia < 100:  
            recarga = min(20, 100 - self.energia)  # Não passa de 100  
            self.energia += recarga  
            print(f"{self.nome} descansa e recupera {recarga} de energia. Energia atual: {self.energia}")  
        else:  
            print(f"{self.nome} já está com energia máxima!")  

    def ver_pontos(self):  
        print(f"Pontuação total de {self.nome}: {self.pontos.pontos}")  

# Função para simular o combate  
def simular_combate(jogador, inimigo):  
    while jogador.energia > 0 and inimigo.vida > 0:  
        jogador.atacar(inimigo)  
        if inimigo.vida > 0:  # Se o inimigo ainda estiver vivo, ele ataca  
            inimigo.atacar(jogador)  

        if jogador.energia <= 0:  # Se a energia acaba, jogador não pode atacar mais  
            print(f"{jogador.nome} não pode atacar. É hora de descansar.")  
            jogador.descansar()  # O jogador descansa ao atingir zero de energia  

# Exemplo de uso  
if __name__ == "__main__":  
    jogador1 = Jogador("Heroi")  
    inimigo1 = Inimigo("Monstro")  

    simular_combate(jogador1, inimigo1)  
    jogador1.ver_pontos()  # Verifica a pontuação após o combate  

    import random  

class Pontuacao:  
    def __init__(self):  
        self.pontos = 0  # Inicializa a pontuação em 0  

    def adicionar_pontos(self, quantidade):  
        self.pontos += quantidade  # Adiciona pontos  
        print(f"Pontos atuais: {self.pontos}")  # Mostra pontuação atual  


class Inimigo:  
    def __init__(self, nome):  
        self.nome = nome  
        self.vida = 100  # Inicializa a vida em 100  

    def atacar(self, alvo):  
        dano = random.randint(5, 20)  # Dano aleatório entre 5 e 20  
        print(f"{self.nome} ataca {alvo.nome} e causa {dano} de dano.")  
        alvo.tomar_dano(dano)  

    def tomar_dano(self, dano):  
        self.vida -= dano  # Reduz a vida pelo valor de dano  
        if self.vida <= 0:  
            self.vida = 0  # Garante que a vida não fique negativa  
            print(f"{self.nome} foi derrotado!")  # Imprime mensagem de derrota  
        else:  
            print(f"Vida de {self.nome} restante: {self.vida}")  


class Jogador:  
    def __init__(self, nome):  
        self.nome = nome  
        self.energia = 100  # Inicializa a energia em 100  
        self.pontos = Pontuacao()  # Inicializa um objeto de pontuação  

    def atacar(self, alvo):  
        if self.energia <= 0:  
            print(f"{self.nome} está sem energia! É necessário descansar para continuar atacando.")  
            return  

        dano = random.randint(5, 20)  # Dano aleatório entre 5 e 20  
        print(f"{self.nome} ataca {alvo.nome} e causa {dano} de dano.")  
        alvo.tomar_dano(dano)  
        self.energia -= 10  # Perde 10 de energia  
        print(f"Energia de {self.nome} restante: {self.energia}")  

        if alvo.vida <= 0:  
            self.pontos.adicionar_pontos(10)  # Adiciona 10 pontos ao derrotar o inimigo  

    def descansar(self):  
        if self.energia < 100:  
            recarga = min(20, 100 - self.energia)  # Não passa de 100  
            self.energia += recarga  
            print(f"{self.nome} descansa e recupera {recarga} de energia. Energia atual: {self.energia}")  
        else:  
            print(f"{self.nome} já está com energia máxima!")  

    def ver_pontos(self):  
        print(f"Pontuação total de {self.nome}: {self.pontos.pontos}")  

def simular_combate(jogador):  
    quantidade_inimigos = random.randint(1, 3)  # Seleciona entre 1 a 3 inimigos  
    inimigos = [Inimigo(f"Inimigo {i + 1}") for i in range(quantidade_inimigos)]  
    
    for inimigo in inimigos:  
        print(f"\nUm {inimigo.nome} apareceu!")  
        while jogador.energia > 0 and inimigo.vida > 0:  
            jogador.atacar(inimigo)  
            if inimigo.vida > 0:  # Se o inimigo ainda estiver vivo, ele ataca  
                inimigo.atacar(jogador)  

        if jogador.energia <= 0:  
            print(f"{jogador.nome} foi derrotado! Fim do jogo.")  
            return False  # O jogador foi derrotado  

    print(f"{jogador.nome} venceu todos os inimigos!")  
    return True  # O jogador venceu todos os inimigos  

class Menu:  
    def __init__(self):  
        self.options = {  
            "1": self.iniciar_jogo,  
            "2": self.mostrar_opcoes,  
            "3": self.sair  
        }  

        import random  

class Inimigo:  
    def __init__(self, nome):  
        self.nome = nome  
        self.vida = 100  # Inicializa a vida em 100  
        self.__forca = random.randint(5, 20)  # Força do ataque, valor aleatório entre 5 e 20  

    def atacar(self, alvo):  
        # Exibe a força do ataque ao invés de um valor aleatório  
        dano = self.__forca  # Usa a força privada para calcular o dano  
        print(f"{self.nome} ataca {alvo.nome} com força {dano} e causa {dano} de dano.")  
        alvo.tomar_dano(dano)  

    def tomar_dano(self, dano):  
        self.vida -= dano  # Reduz a vida pelo valor de dano  
        if self.vida <= 0:  
            self.vida = 0  # Garante que a vida não fique negativa  
            print(f"{self.nome} foi derrotado!")  # Imprime mensagem de derrota  
        else:  
            print(f"Vida de {self.nome} restante: {self.vida}")  

# Exemplo de uso da classe Inimigo  
if __name__ == "__main__":  
    jogador = Jogador("Heroi")  # Exemplificando a interação com Jogador  
    inimigo = Inimigo("Monstro")  

    # Simula um ataque do inimigo ao jogador  
    inimigo.atacar(jogador)  

    