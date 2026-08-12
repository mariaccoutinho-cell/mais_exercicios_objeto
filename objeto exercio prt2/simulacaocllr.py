class Aplicativo:
    def __init__(self, nome, consumo_bateria=100):
        self.nome = nome
        self.consumo_bateria = consumo_bateria


class Celular:
    def __init__(self, modelo, bateria=100):
        self.modelo = modelo
        self.bateria = bateria
        self.ligado = False

    def ligar(self):
        self.ligado = True
        print(f"O {self.modelo} foi ligado.")

    def desligar(self):
        self.ligado = False
        print(f"O {self.modelo} foi desligado.")

    def executar_app(self, app):
        if not self.ligado:
            print(f"Erro: Não é possível executar '{app.nome}'. O celular está desligado.")
            return

        if self.bateria < app.consumo_bateria:
            print(f"Erro: Bateria insuficiente ({self.bateria}%) para rodar '{app.nome}' (requer {app.consumo_bateria}%).")
            return

        self.bateria -= app.consumo_bateria
        print(f"Aplicativo '{app.nome}' executado com sucesso! Consumo: {app.consumo_bateria}%. Bateria restante: {self.bateria}%.")


app_redes_sociais = Aplicativo("Instagram", 25)
app_jogo = Aplicativo("Jogo 3D Pesado", 50)

meu_celular = Celular("Smartphone Galaxy")

meu_celular.ligar()

meu_celular.executar_app(app_redes_sociais)
meu_celular.executar_app(app_jogo)
    