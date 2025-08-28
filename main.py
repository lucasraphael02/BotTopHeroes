import pyautogui
import os
from glob import glob
import time as t
from datetime import datetime, date

from back.Mobilizacao import Mobilizacao
from back.BuscaImagem import BuscaImagem
from back.ChefeDiario import ChefeDiario
from back.ChefeDaGuilda import ChefeDaGuilda
from back.Mitica import PegarMitica






if __name__ == "__main__":
    condicao = True
    while condicao:
        print("1 - Mobs automáticas")
        print("2 - Boss Automático")
        print("3 - Chefe diário Automático")
        print("4 - Calculadora de Horario")
        print("5 - Pegar Míticas")
        print("0 - Sair")
        entrada = input("Escolha: ")
        try:
            entrada = int(entrada)
        except:
            entrada = ''
        match entrada:
            case 1:
                Mobilizacao()
                # break
            case 2:
                ChefeDaGuilda()
                # break
                # boss()
            case 3:
                ChefeDiario()
                # break
            case 4:
                horarioAlvo = input('Digite a data e horario alvo (d H M): ')
                horarioAlvo = datetime.strptime(horarioAlvo, '%d %H %M')
                horarioAlvo = horarioAlvo.replace(
                    month=date.today().month,
                    year=date.today().year
                )
                # print(horarioAlvo)
                diferenca = horarioAlvo - datetime.now()
                print(f'\nFalta -> {diferenca}\n')
                # break
            case 5:
                PegarMitica()
            case 6:
                t.sleep(5)
                pyautogui.press('esc')
            case 0:
                condicao = False
                # break
            case _:
                print("Digite um valor válido")

