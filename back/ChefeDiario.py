from glob import glob
import time as t
import os
import pyautogui

from back.BuscaImagem import BuscaImagem

class ChefeDiario():

    def __init__(self):
        self.findImage = BuscaImagem()
        self.iniciarChefeDiario()
        

    def buscarImagem(self, imagemPath, confidence = 0.8):
        return self.findImage.find_image_on_screen(imagemPath, confidence)

    def clicarNaImagem(self, posicao, tempoEspera: int):
        pyautogui.click(posicao)
        t.sleep(tempoEspera)
        
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
        # print(f'Imagens {imagens}')
        imagensfiltradas = self.filtrarImagens(imagens, escolhaTela)
        # print(f'imagensfiltradas {imagensfiltradas}')
        if len(imagensfiltradas) != 1:
            return None
        return imagensfiltradas[0]
        

    def buscarChefe(self, imagemList):
        for imagem in imagemList:
            posicao = self.buscarImagem(imagem)
            if posicao:
                self.clicarNaImagem(posicao, 1)
                return True
        return False
    
    def buscarBotao(self, imagem, tempoEspera = 1, confidence = 0.8):
        posicao = self.buscarImagem(imagem, confidence)
        if posicao is None:
            # print(f'Imagem {imagem} não encontrada')
            return False
        self.clicarNaImagem(posicao, tempoEspera)
        return True
        

    def chefeDiarioExecucao(self, listaChefes, imagemBotaoAtaque, imagemBotaoComecar, imagemFila):
        
        if not self.buscarChefe(listaChefes):
            return False
        
        if not self.buscarBotao(imagemBotaoAtaque, 1):
            return False
        
        if not self.buscarBotao(imagemFila, 1):
            return False
        
        while not self.buscarBotao(imagemBotaoComecar, 5):
            t.sleep(0.1)

        return True
    
    def iniciarChefeDiario(self):
                
        monitorOrNot = input("Digite 1 para uso no Monitor e 2 para Notebook: ")
        monitorOrNot = int(monitorOrNot)

        fila = input("Digite a fila a ser usada: ")

        qtdVezes = input("Digite a quantidade de vezes de ataques: ")
        qtdVezes = int(qtdVezes)
        qtdVezes = qtdVezes if qtdVezes <= 5 else 5

        escolhaTela = '' 
        match monitorOrNot:
            case 1:
                escolhaTela = 'Monitor'
            case 2:
                escolhaTela = 'Not'
        
        botaoAtaquePath = 'imagens\\ChefesDiarios\\BotoesAtaqueChefe'
        botaoComecarPath = 'imagens\\ChefesDiarios\\BotoesComecarChefe'
        filasPath = 'imagens\\FilasBoss'
        imagensChefesFolder = 'imagens\\ChefesDiarios\\ImagensChefes'

        listaChefes = self.buscarImagensEmPasta(imagensChefesFolder)
        imagemBotaoAtaque = self.definirImagemPorFiltro(imagensPath=botaoAtaquePath, escolhaTela=escolhaTela)
        imagemBotaoComecar = self.definirImagemPorFiltro(imagensPath=botaoComecarPath, escolhaTela=escolhaTela)
        imagemFila = self.definirImagemPorFiltros(imagensPath=filasPath, escolhaTela=escolhaTela, escolhaFila=fila)

        

        i=0
        while i<qtdVezes:
            resultado = self.chefeDiarioExecucao(listaChefes, imagemBotaoAtaque, imagemBotaoComecar, imagemFila)
            if resultado:
                i+=1

        
    
        