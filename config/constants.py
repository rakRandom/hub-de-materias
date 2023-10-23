try:
    from config.imports import BigNumber
except:
    from imports import BigNumber


BARRIER = "================================================================================"

REPETIR = "\nRepetir?:\n"

# =================================================================================================
# ======================================== Main ===================================================
# =================================================================================================


CHOOSE_MAIN_LIST = ('1', '2')
CHOOSE_M_LIST = ('1', '2', '3', '4')
CHOOSE_Q_LIST = ('1')


MAIN_DIALOG_1 = BARRIER + """
||
||          Qual matéria você quer acessar?:
||
||     [1] Matemática:
||
||     - numerosprimos.py
||     - testeprimo.py
||     - fracaosimples.py
||     - mmcemdc.py
||
||     [2] Química:
||
||     - gusmol.py
||
""" + BARRIER + "\nR: "


MAIN_DIALOG_M = BARRIER + """
||
||          Qual programa você quer executar?:
||
||     [1] numerosprimos.py
||     - Dá uma lista de números primos de 2 até o número escolhido.
||
||     [2] testeprimo.py
||     - Testa se um número é primo.
||
||     [3] fracaosimples.py
||     - Retorna a fração geratriz de uma dízima periódica e
||     a fração irredutível de um número decimal.
||
||     [4] mmcemdc.py
||     - Recebe dois números e retorna o MMC e MDC deles.
||
""" + BARRIER + "\nR: "


MAIN_DIALOG_Q = BARRIER + """
||
||          Qual programa você quer executar?:
||
||     [1] gusmol.py
||     - Retorna a quantidade de mol, moléculas e átomos em uma certa
||     quantidade de massa e o peso molécular de uma molécula escolhida
||     pelo usuário.
||
""" + BARRIER + "\nR: "



# =================================================================================================
# ======================================== Numeros Primos =========================================
# =================================================================================================


NUMEROSPRIMOS_DIALOG_1 = BARRIER + """
||
||          Número limite:
||
""" + BARRIER + "\nR: "



# =================================================================================================
# ======================================== Teste Primo ============================================
# =================================================================================================


TESTEPRIMO_DIALOG_1 = BARRIER + """
||
||          Número para ser testado:
||
""" + BARRIER + "\nR: "


TESTEPRIMO_DIALOG_2 = BARRIER + """
||
||          {} {}é primo.
||           
""" + BARRIER + "\n"



# =================================================================================================
# ======================================== Fração Simples =========================================
# =================================================================================================


FRACAOSIMPLES_DIALOG_1 = BARRIER + """
||
||          Dízima Periódica [S] ou [N]?
||
""" + BARRIER + "\nR: "


FRACAOSIMPLES_DIALOG_DP1 = BARRIER + """
||
||          Digite a repetição da dizima: 
||
""" + BARRIER + "\nR: "


FRACAOSIMPLES_DIALOG_DP2 = BARRIER + """
||
||          Quantos zeros existem entre a virgula e a repetição?:
||            
""" + BARRIER + "\nR: "


FRACAOSIMPLES_DIALOG_DP3 = BARRIER + """
||
||          Qual é o número antes da vírgula?:
||            
""" + BARRIER + "\nR: "


FRACAOSIMPLES_DIALOG_DP4 = BARRIER + """
||
||     Fração Geratriz:
||       {}/{}
||
||     Fração Irredutível:
||       {}/{}
||           
""" + BARRIER + "\n"


FRACAOSIMPLES_DIALOG_ND1 = BARRIER + """
||
||          Digite um número decimal:
||           
""" + BARRIER + "\nR: "


FRACAOSIMPLES_DIALOG_ND2 = BARRIER + """
||
||     Fração irredutível de {}: 
||       {}/{}
||           
""" + BARRIER + "\n"



# ============================================================================================
# ======================================== MMC e MDC =========================================
# ============================================================================================


MMCEMDC_DIALOG_1 = BARRIER + """
||
||          Digite dois números separados por um espaço:
||           
""" + BARRIER + "\nR: "



# =================================================================================================
# ======================================== Gusmol =================================================
# =================================================================================================


# Constante de Avogrado
AVOGRADO = BigNumber("6.02") * BigNumber("10") ** BigNumber("23")


# Tabela Periódica contendo a massa atômica de todos os elementos
TABELA_PERIODICA = {
    'H': 1,'He': 4,'Li': 7,'Be': 9,'B': 10.9,'C': 12,'N': 14,'O': 16,'F': 19,'Ne': 20.18,'Na': 23,
    'Mg': 24.31,'Al': 27,'Si': 28,'P': 31,'S': 32,'Cl': 35.45,'Ar': 40,'K': 39,'Ca': 40,'Sc': 44.96,
    'Ti': 47.87,'V': 50.94,'Cr': 52,'Mn': 54.94,'Fe': 55.85,'Co': 59,'Ni': 58.69,'Cu': 63.55,
    'Zn': 65.4,'Ga': 69.72,'Ge': 72.63,'As': 74.92,'Se': 78.96,'Br': 80,'Kr': 83.80,'Rb': 85.47,
    'Sr': 87.62,'Y': 88.91,'Zr': 91.22,'Nb': 92.91,'Mo': 96,'Tc': 98,'Ru': 101,'Rh': 103,'Pd': 106.4,
    'Ag': 108,'Cd': 112.4,'In': 114.8,'Sn': 118.7,'Sb': 121.8,'Te': 127.6,'I': 126.9,'Xe': 131.3,
    'Cs': 132.9,'Ba': 137.3,'La': 138.9,'Ce': 140,'Pr': 140,'Nd': 144.2,'Pm': 145,'Sm': 150.4,'Eu': 152,
    'Gd': 157.3,'Tb': 158.9,'Dy': 162.5,'Ho': 164.9,'Er': 167.3,'Tm': 168.9,'Yb': 173,'Lu': 175,
    'Hf': 178.5,'Ta': 180.9,'W': 183.8,'Re': 186.2,'Os': 190.2,'Ir': 192.2,'Pt': 195,'Au': 197,
    'Hg': 200.59,'Tl': 204.38,'Pb': 207.2,'Bi': 208.98,'Po': 209,'At': 210,'Rn': 222,'Fr': 223,'Ra': 226,
    'Ac': 227,'Th': 232.04,'Pa': 231.03,'U': 238.03,'Np': 237.05,'Pu': 244,'Am': 243,'Cm': 247,'Bk': 247,
    'Cf': 251,'Es': 252,'Fm': 257,'Md': 258,'No': 259,'Lr': 262,'Rf': 267,'Db': 270,'Sg': 271,'Bh': 270,
    'Hs': 277,'Mt': 276,'Ds': 281,'Rg': 280,'Cn': 285,'Nh': 284,'Fl': 289,'Mc': 288,'Lv': 293,'Ts': 294,
    'Og': 294
}


GUSMOL_DIALOG_1 = BARRIER + """
||
||          Digite a composição da molécula:
||           
""" + BARRIER + "\nR: "


GUSMOL_DIALOG_IP = BARRIER + """
||
||          Digite a quantidade de matéria em gramas:
||           
""" + BARRIER + "\nR: "


GUSMOL_DIALOG_LR1 = BARRIER + """
||
||    Existem {:1} mol de moléculas
||    A molécula {} pesa {}u
||    {:0.2e} moléculas de {}
||"""
GUSMOL_DIALOG_LR2 = """||    {:0.2e} átomos de {}"""
GUSMOL_DIALOG_LR3 = """||
""" + BARRIER + "\n"
