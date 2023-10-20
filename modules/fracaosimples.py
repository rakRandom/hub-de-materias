from config.functions import cls, f_mdc
from config.constants import *


class FracaoSimples():
    def fracaosimples(self, tipo):
        cls()
        if tipo[0] == 's' or tipo[0] == 'y':
            dizima = input(FRACAOSIMPLES_DIALOG_DP1)
            cls()
            zeros = input(FRACAOSIMPLES_DIALOG_DP2)
            cls()
            numero = input(FRACAOSIMPLES_DIALOG_DP3)

            try:
                int(dizima)
                int(zeros)
                int(numero)

                1/int(dizima)
            except:
                cls()
                input("ERRO")
            else:
                dizima = int(dizima)
                zeros = int(zeros)
                numero = int(numero)

                denominador:str = ''

                for i in str(dizima):
                    denominador = denominador + '9'
                
                denominador = int(denominador)*(10**zeros)
                numerador = int(dizima + (denominador * numero))

                cls()

                num_mdc = f_mdc(numerador, denominador)

                print(FRACAOSIMPLES_DIALOG_DP4
                      .format(numerador, denominador, int(numerador/num_mdc), int(denominador/num_mdc)))
            
        elif tipo[0] == 'n':
            numero = input(FRACAOSIMPLES_DIALOG_ND1)
            
            try:
                float(numero)
            except:
                cls()
                input("ERRO")
            else:
                numero = float(numero)

                denominador = 10**(len(str(numero - int(numero))))

                numerador = int(numero*denominador)

                num_mdc = f_mdc(numerador, denominador)

                cls()
                input(FRACAOSIMPLES_DIALOG_ND2
                      .format(numero, int(numerador/num_mdc), int(denominador/num_mdc)))
        else:
            cls()
            input('ERRO: Input Invalido!')
