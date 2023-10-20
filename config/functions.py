try:
    from config.imports import *
except:
    from imports import *


# ==================== Calculadora da sequência de fibonnaci ====================
@lru_cache()
def fib(n):
    """Limit recomendation: 256"""
    if n < 2: return n
    return fib(n-1) + fib(n-2)


# ==================== Função para limpar o terminal ====================
def cls():
    try: system('cls')
    except: print("\n- Não foi possível limpar o terminal. -\n")


# //////////////////// Under Construction ////////////////////

# ==================== Temporizador de Tempo de Execução de Funções ====================
def w_ttef(f):
    def w(*a, **k):
        c = time()
        r = f(*a, **k)
        t = time()
        
        print(f"{f.__name__}({a}, {k}) -> {t-c} sec.")
        return r
    return w

# ////////////////////////////////////////////////////////////


# ==================== Calculadora de números primos ====================
@lru_cache()
def f_numerosprimos(limite: int) -> list:
    try: int(limite)
    except: return []
    else:
        limite = int(limite)
        lista_de_primos = []

        primo = True
        for numero in range(2, limite+1):
            for divisor in range(2, numero):
                if numero%divisor == 0:
                    primo = False
            if primo:
                lista_de_primos.append(numero)
            primo = True

        return lista_de_primos


# ==================== Calculadora de MMC ====================
@lru_cache()
def f_mmc(*nl: int) -> list:
    try:
        # num_list
        nl: list = sorted(list(map(int, nl)))
        # prime_list
        pl: list = f_numerosprimos(nl[-1])
        # divisor_list
        dl: list = []
        # outerloop_breaker, whileloop_breaker
        olb, wlb = False, True
        # biggest_divisor, product_of_divisors
        bd, pod = 0, 1
    except: return []
    else:
        while True:
            olb, wlb = False, True
            for n in nl:
                if n > 1: wlb = False
                elif n < 1: break
            if wlb: break
            for n in nl:
                for p in pl:
                    if n%p == 0: bd = p; olb = True; break
                if olb: break
            for i, n in enumerate(nl):
                if n%bd == 0: nl[i] = n/bd
            dl.append(bd)
        for n in dl: pod*=n
        return [*dl, pod]


# ==================== Calculadora de MDC ====================
@lru_cache()
def f_mdc(*num_list: int) -> list:
    try:
        # num_list
        num_list: list = sorted(list(map(int, num_list)))
        # prime_list
        prime_list: list = f_numerosprimos(num_list[-1])
        # divisor_list
        divisors_list: list = [1]
        # outerloop_breaker, whileloop_breaker
        outerloop_breaker, whileloop_breaker = False, True
        # biggest_divisor, product_of_divisors
        biggest_divisor, product_of_divisors = 0, 1
    except: return []
    else:
        

        for number in set(divisors_list): 
            product_of_divisors*=number

        return [*set(divisors_list), product_of_divisors]
print(f_mdc(18, 12, 4))
print(f_mdc(2, 4, 3))

# 18 = 2 * 3 * 3 -> 1, 2, 3
# 12 = 2 * 2 * 3 -> 1, 2, 3
# 4 = 2 * 2 -> 1, 2
# MDC(18, 12, 4) = 1 * 2 = 2

# 2 = 2 -> 1, 2
# 4 = 2 * 2 -> 1, 2
# 3 = 3 -> 1, 3
# MDC(2, 4, 3) = 1
