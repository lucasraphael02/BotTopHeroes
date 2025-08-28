from glob import glob
import time as t
import os
import pyautogui

from back.BuscaImagem import BuscaImagem

class Mobilizacao():

    def __init__(self):
        self.findImage = BuscaImagem()
        image_Filas_folder = "imagens\\Mobilizacao\\Filas"  # Substitua pelo caminho da sua pasta
        self.imagemLupaPath = "imagens\\Mobilizacao\\Lupa.png"
        self.imagemProcurarPath = "imagens\\Mobilizacao\\ProcurarBotton.png"
        self.imagemMobilizacaoPath = "imagens\\Mobilizacao\\MobilizacaoBotton.png"
        self.imagemComecarPath = "imagens\\Mobilizacao\\ComecarBotton.png"
        confidence = 0.9  # Nível de confiança para correspondência

        # Lista todas as imagens na pasta (extensões comuns)
        imagemExtensao = ["*.png", "*.jpg", "*.jpeg"]
        image_paths = []
        for ext in imagemExtensao:
            image_paths.extend(glob(os.path.join(image_Filas_folder, ext)))

        if not image_paths:
            print("Nenhuma imagem encontrada na pasta especificada.")
            return
        
        self.iniciarMobilizacao(image_paths, confidence)
        
    def buscarImagem(self, imagemPath, confidence = 0.9):
        return self.findImage.find_image_on_screen(imagemPath, confidence)
    
    def clicarNaImagem(self, posicao, tempoEspera: int):
        pyautogui.click(posicao)
        t.sleep(tempoEspera)
            

    def buscarFila(self, imagePaths, confidence = 0.9):
        for imagePath in imagePaths:
            posicaoFila = self.buscarImagem(imagePath, confidence)
            if posicaoFila:
                print(f"Imagem {imagePath} encotrada na posicao {posicaoFila}")
                return True
        else:
            print("Nenhuma imagem encontrada")    
        return False

    def buscarBotao(self, imagemPath, confidence = 0.8, tempoEspera = 0.5):
        posicaoBotaoProcurar = self.buscarImagem(imagemPath, confidence)
        if posicaoBotaoProcurar is None:
            print(f"Imagem {imagemPath} não encontrada")
            return False
        self.clicarNaImagem(posicaoBotaoProcurar, tempoEspera)
        return True
    
    def executaMobilizacao(self, image_paths, confidence = 0.9):
        
        if not self.buscarFila(image_paths):
            return False
        # return False
        if not self.buscarBotao(self.imagemLupaPath):
            return False
        
        if not self.buscarBotao(self.imagemProcurarPath, tempoEspera=1):
            return False
        
        if not self.buscarBotao(self.imagemMobilizacaoPath):
            return False
        
        if not self.buscarBotao(self.imagemComecarPath):
            pyautogui.press('esc')
            return False

        return True 
    
    def iniciarMobilizacao(self, image_paths, confidence = 0.9):
        i=0
        quantidadeDeMobilizacoes = input("Digite o valor de mobs: ")
        quantidadeDeMobilizacoes = int(quantidadeDeMobilizacoes)
        while i<quantidadeDeMobilizacoes:
            retorno = self.executaMobilizacao(image_paths, confidence)
            tempoEspera = 0.5
            if retorno:
                i+=1
                print(f"Iteração {i}")
                tempoEspera = 1
            t.sleep(tempoEspera)
        print("Acabou")