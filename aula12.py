# Modelagem e Abstração - Forma do Biscoito
import time
class thinkphone:
    def __init__(self, ano: float, modelo: str, tela: str, processador: str, memoria: float, armazenamento: float, camera: float, sistema: str, bateria: float, conectividade: float, sensor: str, biometria: str, design: str, audio: str):
        self.modelo = modelo
        self.ano = ano
        self.tela = tela
        self.processador = processador
        self.memoria = memoria
        self.armazenamento = armazenamento 
        self.cameras = camera
        self.sistema = sistema
        self.bateria = bateria
        self.conectividade = conectividade
        self.sensor = sensor
        self.biometria = biometria
        self.design = design 
        self.audio = audio 
        self. ligado = False

    def ligar (self):
        if not self.ligado:
            self.ligado = True
            time.sleep(5)
            print (f'{self.modelo} foi LIGADO')
        else:
            print (f'{self.modelo} já está ligado!')
    

    def ligar (self):
        if not self.ligado:
            self.ligado = True
            time.sleep(5)
            print (f'{self.modelo} foi DESLIGADO')
        else:
            print (f'{self.modelo} já está desligado!')

    def exibir_info (self):
        print (f'''
            Celular: {self.marca}{self.modelo}
            Armazenamento: {self.armazenamento}
            Status: {'Sim' if self.ligado else 'Não'}
               
     ''')
    

    def modelo(self):
            
        return f' hello thinkphone, versão {self.ano}. Modelo: tela de {self.tela}, processador de {self.processador}, memória de {self.memoria}, {self.sistema}, {self.armazenamento} de armazenamento, câmera de {self.cameras}, sistema {self.sistema}, bateria {self.bateria} com conectividade{self.conectividade}. Seu sensor é {self.sensor}, {self.biometria} biometria, design {self.design}, áudio {self.audio}'

# Instanciar o Objeto - A Massa do Biscoito
thinkphone1 = thinkphone (2025, "grande", "jyp", "snapdragon", 2, 24, 24, "[otimo]", 3000, "massa", 5, "sim", "sim", "sim")
thinkphone2 = thinkphone (2026, "grande", "yg", "snapdragon", 2, 24, 24, "[otimo]", 3000, "massa", 5, "sim", "sim", "sim")
thinkphone3 = thinkphone (2027, "grande", "cube" "snapdragon", 2, 24, 24, "[otimo]", 3000, "massa", 5, "sim", "sim", "sim")

print (thinkphone1.ligar())
print (thinkphone1.exibir_info())


