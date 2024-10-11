class Tamagochi:
    def __init__(self, nome):
        self.estado = "parado"
        self.nome = nome

    def comer(self):
        if self.estado == "parado":
            self.estado = "comendo"
            print(f"{self.nome} está comendo.")
            self.estado = "parado"
            print(f"{self.nome} parou de comer")
        else:
            print(f"{self.nome} não pode comer agora, ele está {self.estado}")

    def andar(self):
        if self.estado == "parado":
            self.estado = "andando"
            print(f"{self.nome} está andando.")
            self.estado = "parado"
            print(f"{self.nome} parou de andar")
        else:
            print(f"{self.nome} não pode andar agora, ele está {self.estado}")

    def dormir(self):
        if self.estado == "parado":
            self.estado = "dormindo"
            print(f"{self.nome} está dormindo.")
            self.estado = "parado"
            print(f"{self.nome} acordou!")
        else:
            print(f"{self.nome} não pode dormir agora, ele está {self.estado}")
