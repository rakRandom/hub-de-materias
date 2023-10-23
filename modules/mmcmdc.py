from config.functions import cls, f_mdc, f_mmc
from config.constants import *


class MmcMdc():
    def mmcmdc(self, numeros: str):
        try:
            numeros = tuple(map(int, numeros.split(' ')))
        except:
            cls()
            print('ERRO')
        else:
            mdc_list = f_mdc(*numeros)
            mdc = mdc_list[-1]
            mdc_list.pop()

            mmc_list = f_mmc(*numeros)
            mmc = mmc_list[-1]
            mmc_list.pop()

            cls()
            print("MDC:")
            for e in mdc_list:
                print(e, end=" * ")
            print(f"1 = {mdc}\n")

            print("MMC:")
            for e in mmc_list:
                print(e, end=" * ")
            print(f"1 = {mmc}")
            input()
