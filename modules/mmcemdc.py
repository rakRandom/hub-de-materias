from config.functions import cls, f_mdc, f_mmc
from config.constants import *


class MmcEMdc():
    def mmcemdc(self, numeros: str):
        try:
            numero1, *_, numero2 = numeros.split(' ')
        except:
            cls()
            print('ERRO')
        else:
            numero1, *_, numero2 = numeros.split(' ')

            print(numero1, numero2)
            input()
