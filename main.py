"""Objetivo:
Criação de um hub com toda a informação que eu possa imaginar, principalmente calculadoras.
Feito sozinho, porém com a ajuda de diversas pessoas anônimas, por meio de ferramentas como o GitHub¹,
StackOverFlow² e YouTube³. Toda a documentação e arquivos estão no meu repositório⁴ do GitHub.

Feito por: Fellipe Leonardo Peixoto Cunha

Data de inicio: 07/10/2023
Data de lançamento: XX/XX/20XX

Referências:
1. https://github.com/rakRandom
2. https://stackoverflow.com/users/22330138
3. https://www.youtube.com/channel/UCjeFvSx21Sp3C1aP5r31M-A
4. https://github.com/rakRandom/hub-de-materias
"""


# ---------------------------------------------------------------------------------------------------------------------------------------------------
# ---------------------------- BEGGINING OF IMPORTANT AREA - DO NOT CHANGE --------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------------------------------------

# ==================== Configurações ====================
try:
    from config.constants import *
    from config.imports import *
    from config.functions import cls, LazyImport
except: raise ImportError()

# ==================== Matemática ====================
try:
    imp_numerosprimos = LazyImport("modules.numerosprimos")
    imp_testeprimo = LazyImport("modules.testeprimo")
    imp_fracaosimples = LazyImport("modules.fracaosimples")
    imp_mmcmdc = LazyImport("modules.mmcmdc")
except: raise ImportError()

# ==================== Química ====================
try:
    imp_gusmol = LazyImport("modules.gusmol")
except: raise ImportError()


# ========== Objetos ==========
obj_numerosprimos: Any | None = None
obj_testeprimo   : Any | None = None
obj_fracaosimples: Any | None = None
obj_mmcmdc       : Any | None = None
obj_gusmol       : Any | None = None

choose: str = ""


# ==================== Execução ====================
if __name__ == "__main__":
    while True:
        cls()
        while True:
            choose = str(input(MAIN_DIALOG_1)).lower()
            cls()
            if len(choose) > 0:
                if choose in CHOOSE_MAIN_LIST: break
                elif choose == "exit" or choose == '': exit()

# ---------------------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------- END OF IMPORTANT AREA - DO NOT CHANGE -----------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------------------------------------

        if choose == '1':
            while True:
                choose = str(input(MAIN_DIALOG_M))
                if choose in CHOOSE_M_LIST or choose == '': break
            
            if choose == '1':
                if obj_numerosprimos is None: obj_numerosprimos = imp_numerosprimos.NumerosPrimos()

                while True:
                    cls()
                    obj_numerosprimos.numerosprimos(input(NUMEROSPRIMOS_DIALOG_1))

                    if str(input(REPETIR)).lower()[0] != 's': break

            elif choose == '2':
                if obj_testeprimo is None: obj_testeprimo = imp_testeprimo.TestePrimo()

                while True:
                    cls()
                    obj_testeprimo.testeprimo(input(TESTEPRIMO_DIALOG_1))

                    if str(input(REPETIR)).lower()[0] != 's': break

            elif choose == '3':
                if obj_fracaosimples is None: obj_fracaosimples = imp_fracaosimples.FracaoSimples()

                while True:
                    cls()
                    obj_fracaosimples.fracaosimples(str(input(FRACAOSIMPLES_DIALOG_1)).lower())

                    if str(input(REPETIR)).lower()[0] != 's': break
            
            elif choose == '4':
                if obj_mmcmdc is None: obj_mmcmdc = imp_mmcmdc.MmcMdc()

                while True:
                    cls()
                    obj_mmcmdc.mmcmdc(str(input(MMCEMDC_DIALOG_1)).lower())

                    if str(input(REPETIR)).lower()[0] != 's': break


# =======================================================================================================

        elif choose == '2':
            while True:
                choose = str(input(MAIN_DIALOG_Q))
                if choose in CHOOSE_Q_LIST or choose == '': break
            
            if choose == '1':
                if obj_gusmol is None: obj_gusmol = imp_gusmol.Gusmol()

                while True:
                    cls()
                    obj_gusmol.gusmol(''.join(str(input(GUSMOL_DIALOG_1)).split()))
                    
                    if str(input(REPETIR)).lower()[0] != 's': break
