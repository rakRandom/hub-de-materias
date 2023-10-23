from config.functions import cls
from config.constants import *


class Gusmol():
    new_element:str = ''

    def gusmol(self, molecula: str):
        if len(molecula) > 0:
            if molecula[0].isupper():

                # Definindo as variáveis
                elementos:dict = {}

                peso_molecular:int = 0

                upper:bool = False
                number:bool = False

                # Filtrando os átomos e os seus valores
                for i in molecula:
                    try:
                        int(i)
                    except:
                        number = False
                        if i.isupper() and not upper:
                            save = i
                            upper = True
                        elif i.isupper() and upper:
                            elementos[save] = 1
                            save = i
                        elif i.islower():
                            elementos[save + i] = 1
                            upper = False
                            self.new_element = save+i
                    else:
                        if not number:
                            if upper:
                                elementos[save] = i
                                upper = False

                                self.new_element = save
                            else:
                                elementos[self.new_element] = i
                        else:
                            elementos[self.new_element] = int(elementos[self.new_element])*10 + int(i)
                        
                        number = True
                if upper:
                    elementos[save] = 1

                # Calculando o peso da molécula
                for i, e in enumerate(list(elementos.items())):
                    try:
                        TABELA_PERIODICA[e[0]]
                    except:
                        cls()
                        save = 'erro'
                        break
                    else:
                        peso_molecular += TABELA_PERIODICA[e[0]]*int(e[1])
                
                if save != 'erro':
                    # Input do peso
                    cls()
                    massa = input(GUSMOL_DIALOG_IP)

                    try:
                        int(massa)
                        1/int(massa)
                    except:
                        cls()
                        input("ERRO")
                    else:
                        massa = int(massa)

                        # Calculando Mol
                        mol = massa/peso_molecular
                        if mol - int(mol) == 0:mol = int(mol)

                        # Lançando o resultado
                        cls()
                        print(GUSMOL_DIALOG_LR1
                            .format(mol, molecula, peso_molecular, int(BigNumber(mol)*AVOGRADO), molecula))
                        
                        for i, e in enumerate(list(elementos.items())):
                            quantidade = int(BigNumber(mol)*AVOGRADO)*int(e[1])
                            print(GUSMOL_DIALOG_LR2.format(quantidade, e[0]))
                        input(GUSMOL_DIALOG_LR3)
                else:
                    cls()
                    input("ERRO")
            else:
                cls()
                input("ERRO")
        else:
            cls()
            input("ERRO")
