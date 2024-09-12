class Plantas:
    def __init__(self, nome, nome_cientifico, genero, grupo):
        self.nome = nome
        self.nome_cientifico = nome_cientifico
        self.genero = genero
        self.grupo = grupo
        self.extinta = False

    def __str__(self):
        return (f"Nome: {self.nome}, Nome Científico: {self.nome_cientifico}, "
                f"Gênero: {self.genero}, Grupo: {self.grupo}, Extinta: {self.extinta}")

planta_Goiaba = Plantas("Goiaba", "Psidium guajava", "Psidium", "Angiosperma")
planta_Acerola = Plantas("Acerola", "Malpighia emarginata", "Malpighia", "Angiosperma")
planta_Pitaia = Plantas("Pitaia", "Hylocereus spp.", "Hylocereus", "Cactácea")

plantas = {planta_Goiaba, planta_Acerola, planta_Pitaia}

print(planta_Acerola)
print(planta_Goiaba)
