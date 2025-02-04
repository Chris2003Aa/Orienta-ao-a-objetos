class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.velocidade = 0  # Inicialmente, o carro está parado

    def acelerar(self, quantidade):
        self.velocidade += quantidade
        print(f"{self.modelo} acelerou para {self.velocidade} km/h.")

    def frear(self, quantidade):
        self.velocidade -= quantidade
        if self.velocidade < 0:
            self.velocidade = 0  # A velocidade não pode ser negativa
        print(f"{self.modelo} freou para {self.velocidade} km/h.")

    def exibir_detalhes(self):
        print(f"Carro: {self.marca} {self.modelo}, Ano: {self.ano}, Velocidade: {self.velocidade} km/h")


# Criando alguns carros
carro1 = Carro("Toyota", "Corolla", 2022)
carro2 = Carro("Honda", "Civic", 2021)
carro3 = Carro("Ford", "Mustang", 2023)

# Testando os métodos
carro1.exibir_detalhes()
carro1.acelerar(50)
carro1.frear(20)
carro1.exibir_detalhes()

print("\n")

carro2.exibir_detalhes()
carro2.acelerar(80)
carro2.frear(50)
carro2.exibir_detalhes()

print("\n")

carro3.exibir_detalhes()
carro3.acelerar(100)
carro3.frear(120)  # Testando se a velocidade não fica negativa
carro3.exibir_detalhes()
