"""Espaço para testes

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


----------------------------------------- Sections Markers -----------------------------------------
"""

# from functools import lru_cache
# from time import time

# def timeit(func):
#     def timed(*args, **kwargs):
#         t = time()
#         r = func(*args, **kwargs)
#         print(time() - t)

#         return r
#     return timed

# @timeit
# @lru_cache(maxsize=None)
# def fib(n):
#     if n < 2: return n
#     return fib(n-1) + fib(n-2)

# print(fib(256))
