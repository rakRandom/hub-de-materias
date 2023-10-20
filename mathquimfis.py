"""Objetivo:
Treinamento do módulo pygame, com a criação de um jogo do tipo endless runner
chamado "Runneer", usando como referência e auxílio o vídeo "The ultimate introduction to Pygame"¹

Feito por: Fellipe Leonardo Peixoto Cunha²

Data de inicio: 07/10/2023
Data de lançamento: XX/XX/20XX

Referências:

1. https://www.youtube.com/watch?v=AY9MnQ4x3zk
2. https://github.com/rakRandom
3. https://www.youtube.com/@ClearCode
4. https://github.com/clear-code-projects

----------------------------------------- Sections Markers -----------------------------------------

Only shows the name of a sub-section - lowest importance - indented
- '=' 10 times after and before the name
# ========== Area ==========


Only shows the name of a section - low importance - indented
- '=' 20 times after and before the name
# ==================== Area ====================


Shows the name of a section and that it is not complete or usable - medium importance - indented
- '/' 20 times after and before the name
- '/' 60 times when closing the section
# //////////////////// Under Construction ////////////////////
# ////////////////////////////////////////////////////////////


Shows the name of a section and that it is complete - high importance - indentless
- 100 col length in total
# --------------------------------------------- Area ----------------------------------------------


Shows that the area is totally complete and only change it to expand with caution - highest importance - indentless
- '-' 147 times on the line above and below
- '-' 28 times after, 'BEGGINING OF IMPORTANT AREA - DO NOT CHANGE' in the middle and '-' 74 times after
- '-' 31 times after, 'END OF IMPORTANT AREA - DO NOT CHANGE' in the middle and '-' 77 times after
# ---------------------------------------------------------------------------------------------------------------------------------------------------
# ---------------------------- BEGGINING OF IMPORTANT AREA - DO NOT CHANGE --------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------- END OF IMPORTANT AREA - DO NOT CHANGE -----------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------------------------------------


----------------------------------------- Sections Markers -----------------------------------------"""


# ---------------------------------------------------------------------------------------------------------------------------------------------------
# ---------------------------- BEGGINING OF IMPORTANT AREA - DO NOT CHANGE --------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------------------------------------

# ==================== Configurações ====================
try:
    from config.constants import *
    from config.imports import *
    from config.functions import *
except: raise ImportError()

# ==================== Matemática ====================
try:
    from modules.numerosprimos import NumerosPrimos
    from modules.testeprimo import TestePrimo
    from modules.fracaosimples import FracaoSimples
    from modules.mmcemdc import MmcEMdc
except: raise ImportError()

# ==================== Química ====================
try:
    from modules.gusmol import Gusmol
except: raise ImportError()


# ========== Objetos ==========
numerosPrimos = NumerosPrimos()
testePrimo = TestePrimo()
fracaoSimples = FracaoSimples()
mmcEMdc = MmcEMdc()
gusmol = Gusmol()

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
                while True:
                    cls()
                    numerosPrimos.numerosprimos(input(NUMEROSPRIMOS_DIALOG_1))

                    if str(input(REPETIR)).lower()[0] != 's': break

            elif choose == '2':
                while True:
                    cls()
                    testePrimo.testeprimo(input(TESTEPRIMO_DIALOG_1))

                    if str(input(REPETIR)).lower()[0] != 's': break

            elif choose == '3':
                while True:
                    cls()
                    fracaoSimples.fracaosimples(str(input(FRACAOSIMPLES_DIALOG_1)).lower())

                    if str(input(REPETIR)).lower()[0] != 's': break
            
            elif choose == '4':
                while True:
                    cls()
                    mmcEMdc.mmcemdc(str(input(MMCEMDC_DIALOG_1)).lower())

                    if str(input(REPETIR)).lower()[0] != 's': break


# =======================================================================================================

        elif choose == '2':
            while True:
                choose = str(input(MAIN_DIALOG_Q))
                if choose in CHOOSE_Q_LIST or choose == '':break
            
            if choose == '1':
                while True:
                    cls()
                    gusmol.gusmol(''.join(str(input(GUSMOL_DIALOG_1)).split()))
                    
                    if str(input(REPETIR)).lower()[0] != 's': break
