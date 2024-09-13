class Jogos:
    jogos = []  

    def __init__(self, nome, desenvolvedor, genero, ano_lancamento, estoque):
        self.nome = nome
        self.desenvolvedor = desenvolvedor
        self.genero = genero
        self.ano_lancamento = ano_lancamento
        self._estoque = estoque

        Jogos.jogos.append(self)

    def __str__(self):
        return (f'{self.nome} | {self.desenvolvedor} | {self.genero} | {self.ano_lancamento} | {self.estoque}')

    @staticmethod
    def listar_jogos():
        
        for jogo in Jogos.jogos:
            print(jogo)

    @property
    def estoque(self):
        return 'Sem estoque' if not self._estoque else 'Em estoque'

jogo_The_Witcher = Jogos("The Witcher 3: Wild Hunt", "CD Projekt Red", "RPG", 2015, True)
jogo_Cyberpunk = Jogos("Cyberpunk 2077", "CD Projekt Red", "RPG", 2020, False)
jogo_Hades = Jogos("Hades", "Supergiant Games", "Roguelike", 2020, True)

Jogos.listar_jogos()
