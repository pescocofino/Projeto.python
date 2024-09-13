class Jogos:
    jogos = []  

    def __init__(self, nome, desenvolvedor, genero, ano_lancamento):
        self.nome = nome
        self.desenvolvedor = desenvolvedor
        self.genero = genero
        self.ano_lancamento = ano_lancamento
        Jogos.jogos.append(self)

    def __str__(self):
        return (f'{self.nome} | {self.desenvolvedor} | {self.genero} | {self.ano_lancamento}')

    @staticmethod
    def listar_jogos():
        for jogo in Jogos.jogos:
            print(jogo)


jogo_The_Witcher = Jogos("The Witcher 3: Wild Hunt", "CD Projekt Red", "RPG", 2015)
jogo_Cyberpunk = Jogos("Cyberpunk 2077", "CD Projekt Red", "RPG", 2020)
jogo_Hades = Jogos("Hades", "Supergiant Games", "Roguelike", 2020)


Jogos.listar_jogos()
