import random


class PetVirtual:

    def __init__(self, nome, fome=5, felicidade=5):
        self.nome = nome
        self.fome = fome
        self.felicidade = felicidade

    def _perda_aleatoria_felicidade(self):

        perda = random.randint(0, 2)
        self.felicidade = max(0, self.felicidade - perda)

    def alimentar(self):
        if self.fome == 0:
            print(f"[{self.nome}] Ele está cheio!")
        else:
            self.fome = max(0, self.fome - 2)
            print(f"[{self.nome}] Alimentado! Fome atual: {self.fome}")

        self._perda_aleatoria_felicidade()

    def brincar(self):
        self.felicidade += 2
        self.fome += 1
        self._perda_aleatoria_felicidade()
        print(
            f"[{self.nome}] Brincou! Felicidade: {self.felicidade} | Fome: {self.fome}"
        )

    def status(self):
        self._perda_aleatoria_felicidade()
        print(
            f"--- STATUS DE {self.nome.upper()} ---\nFelicidade: {self.felicidade} | Fome: {self.fome}\n"
        )


meu_pet = PetVirtual("Pou")

meu_pet.status()

meu_pet.brincar()
meu_pet.brincar()

meu_pet.alimentar()
meu_pet.alimentar()
meu_pet.alimentar()

meu_pet.status()