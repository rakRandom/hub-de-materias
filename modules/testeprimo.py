from config.functions import cls
from config.constants import *


class TestePrimo():
    save:str = ''

    def testeprimo(self, numero):
        try:
            int(numero)
        except:
            cls()
            input("ERRO")
        else:
            numero = int(numero)

            toggle = True
            if numero%2 != 0 or numero == 2:
                for i in range(3, numero):
                    if numero%(i) == 0:
                        toggle = False
                        break
            else: toggle = False
        
            cls()

            if toggle and numero != 1:
                self.save = ''
            else:
                self.save = 'não '
            
            input(TESTEPRIMO_DIALOG_2.format(numero, self.save))
