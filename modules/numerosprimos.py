from config.functions import cls, f_numerosprimos
from config.constants import *


class NumerosPrimos():
    def numerosprimos(self, limite):
        try:
            lista_de_primos = f_numerosprimos(int(limite))
        except:
            cls()
            input("ERRO")
        else:
            cls()
            print(*lista_de_primos, sep=", ", end=", ")
            input('...\n')
