from glob import glob
import time as t
import os
import pyautogui
from datetime import datetime, date, timedelta

from back.BuscaImagem import BuscaImagem

class ChefeDaGuilda():

    def __init__(self):
        self.findImage = BuscaImagem()
        self.iniciarChefeDaGuilda()

    def buscarImagem(self, imagemPath, confidence = 0.8):
        return self.findImage.find_image_on_screen(imagemPath, confidence)

    def clicarNaImagem(self, posicao, tempoEspera: int):
        pyautogui.click(posicao)
        t.sleep(tempoEspera)

    def buscarBotao(self, imagem, tempoEspera = 1, confidence = 0.8):
        posicao = self.buscarImagem(imagem, confidence)
        if posicao is None:
            # print(f'Imagem {imagem} não encontrada')
            return False
        self.clicarNaImagem(posicao, tempoEspera)
        return True

    def buscarImagensEmPasta(self, imagemPath):
        image_extensions = ["*.png", "*.jpg", "*.jpeg"]
        image_paths = []
        for ext in image_extensions:
            image_paths.extend(glob(os.path.join(imagemPath, ext)))
        return image_paths
    
    def filtrarImagens(self, listaImagens, escolha):
        return [n for n in listaImagens if escolha in n]

    def definirImagemPorFiltros(self, imagensPath, escolhaTela, escolhaFila):
        imagens = self.buscarImagensEmPasta(imagensPath)
        imagensfiltradas = self.filtrarImagens(imagens, escolhaFila)
        imagensfiltradas = self.filtrarImagens(imagensfiltradas, escolhaTela)
        if len(imagensfiltradas) != 1:
            return None
        return imagensfiltradas[0]
    
    def definirImagemPorFiltro(self, imagensPath, escolhaTela):
        imagens = self.buscarImagensEmPasta(imagensPath)
        imagensfiltradas = self.filtrarImagens(imagens, escolhaTela)
        if len(imagensfiltradas) != 1:
            return None
        return imagensfiltradas[0]

    def iniciarChefeDaGuilda(self):
        
        monitorOrNot = input("Digite 1 para uso no Monitor e 2 para Notebook: ")
        monitorOrNot = int(monitorOrNot)

        fila = input("Digite a fila a ser usada: ")

        horarioInicio = input("Digite o Horario de Inicio do Boss (HH MM): ")

        horarioInicio = datetime.strptime(horarioInicio, "%H %M")
        horarioInicio = horarioInicio.replace(
            year=date.today().year,
            month=date.today().month,
            day=date.today().day
        )

        horarioFinal = horarioInicio + timedelta(minutes=30)
        # diferenca = horarioInicio - datetime.now()

        # print(horarioInicio)
        # print(horarioFinal)
        # return
        
        escolhaTela = '' 
        match monitorOrNot:
            case 1:
                escolhaTela = 'Monitor'
            case 2:
                escolhaTela = 'Not'
    
        # t.sleep(diferenca.total_seconds())

        imagensChefePath = 'imagens\\BossDaGuilda\\ImagensChefeDaGuilda'
        imagensBotaoMobilizacao = 'imagens\\BossDaGuilda\\BotoesMobilizacao'
        imagensBotaoIniciarPath = 'imagens\\BossDaGuilda\\BotoesIniciarMobilizacao'
        imagensFilasBossPath = 'imagens\\FilasBoss'
        imagensBotaoComecarPath = 'imagens\\BossDaGuilda\\BotoesComecar'

        imagemChefe = self.definirImagemPorFiltro(imagensChefePath, escolhaTela)
        imagemBotaoMobilizacao = self.definirImagemPorFiltro(imagensBotaoMobilizacao, escolhaTela)
        imagemBotaoIniciar = self.definirImagemPorFiltro(imagensBotaoIniciarPath, escolhaTela)
        imagemFilaBoss = self.definirImagemPorFiltros(imagensFilasBossPath, escolhaTela, fila)
        imagemBotaoComecar = self.definirImagemPorFiltro(imagensBotaoComecarPath, escolhaTela)

        
        
        while datetime.now() < horarioFinal:
            self.execucaoChefeDaGuilda(imagemChefe, imagemBotaoMobilizacao, imagemBotaoIniciar, imagemFilaBoss, imagemBotaoComecar)


    def execucaoChefeDaGuilda(self, imagemChefe, imagemBotaoMobilizacao, imagemBotaoIniciar, ImagemFilaBoss, imagemBotaoComecar):

        if not self.buscarBotao(imagemChefe, 2):
            return False
        
        if not self.buscarBotao(imagemBotaoMobilizacao, 2):
            return False
        
        if not self.buscarBotao(imagemBotaoIniciar, 2):
            return False
        
        if not self.buscarBotao(ImagemFilaBoss, 2):
            return False
        
        while not self.buscarBotao(imagemBotaoComecar, 40):
            t.sleep(0.1)

        return True