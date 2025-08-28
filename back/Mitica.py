from glob import glob
import time as t
import os
import pyautogui
import threading

from back.BuscaImagem import BuscaImagem

class PegarMitica():
    def __init__(self):
        self.findImage = BuscaImagem()
        self.botaoJuntarSePath = 'imagens\\Miticas\\BotaoJuntarSe.png'
        self.condicaoParada = True
        self.pegarMiticas()


    def buscarImagem(self, imagemPath, confidence = 0.9):
        return self.findImage.find_image_on_screen(imagemPath, confidence)
    
    def clicarNaImagem(self, posicao, tempoEspera: float):
        pyautogui.click(posicao)
        t.sleep(tempoEspera)

    def pegarMiticas(self):
        thread = threading.Thread(target=self.executaAcao)
        thread.start()
        while self.condicaoParada:
            resposta = input("Continuar pegando miticas? (y/n)")
            if resposta.lower() == 'n':
                self.condicaoParada = False
    

    def executaAcao(self):
        while self.condicaoParada:
            posicao = self.buscarImagem(self.botaoJuntarSePath, 0.8)
            if not posicao:
                t.sleep(0.1)
            else:
                self.clicarNaImagem(posicao, 0.1)