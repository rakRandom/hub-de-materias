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
# def w_ttef(f):
#     def w(*a, **k):
#         c = time()
#         r = f(*a, **k)
#         t = time()
        
#         print(f"{f.__name__}({a}, {k}) -> {t-c} sec.")
#         return r
#     return w

# ////////////////////////////////////////////////////////////


# ==================== Retorna a quantidade de KBs que o programa está utilizando ====================
def mug() -> float:
    proc: Process = Process(getpid())
    return proc.memory_info().rss / 1024


class LazyImport:
    def __init__(self, module_name: str, package_name: str | None = None):
        self.module_name: str = module_name
        self.package_name: str | None = package_name
        self.__module: Any | None = None
    
    def __getattr__(self, attr: str) -> Any:
        if self.__module is None:
            if self.package_name is None:
                self.__module = import_module(self.module_name)
            else:
                self.__module = import_module(self.module_name, self.package_name)
        return getattr(self.__module, attr)


# ==================== Calculadora de números primos ====================
@lru_cache()
def f_numerosprimos(n: int) -> list:
    try: int(n)
    except: return []
    else:
        # n = int(n)
        # lista_de_primos = []

        # primo = True
        # for numero in range(2, n+1):
        #     for divisor in range(2, numero):
        #         if numero%divisor == 0:
        #             primo = False
        #     if primo:
        #         lista_de_primos.append(numero)
        #     primo = True

        # return lista_de_primos

        sieve = np.ones(n//3 + (n%6==2), dtype=bool)
        for i in range(1,int(n**0.5)//3+1):
            if sieve[i]:
                k=3*i+1|1
                sieve[       k*k//3     ::2*k] = False
                sieve[k*(k-2*(i&1)+4)//3::2*k] = False
        return np.r_[2,3,((3*np.nonzero(sieve)[0][1:]+1)|1)]


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
        bd = 0
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
        return [*dl, reduce(lambda a, b: a * b, dl)]


# ==================== Calculadora de MDC ====================
@lru_cache()
def f_mdc(*nl: int) -> list:
    try:
        # num_list
        nl: list = sorted(list(map(int, nl)))
        # prime_list
        pl: list = f_numerosprimos(nl[-1])
        # divisor_list
        dl: list = []
    except: return []
    else:
        for i, n in enumerate(nl):
            dl.append([1])
            while True:
                for p in pl:
                    if n % p == 0:
                        n = int(n/p)
                        dl[i].append(p)
                        break
                if n == 1: break
        dl = list(map(list, list(map(set, dl))))
        dl = [sb + [1] * (max(len(sb) for sb in dl) - len(sb)) for sb in dl]
        dl = np.array(sum(np.array(dl).tolist(), []))
        dl = set(list(filter(lambda x: (np.count_nonzero(dl == x) >= len(nl)), dl)))
        return [*dl, reduce(lambda a, b: a * b, dl)]

