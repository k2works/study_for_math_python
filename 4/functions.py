'''
級数を出力
x + x**2 + x**3 + ... + x**n
    ---    ---          ---
     2      3            n
xの値で級数の値を計算
'''
from sympy import Symbol, pprint, init_printing
def print_series(n):

    # 出力を逆順に初期化
    init_printing(order='rev-lex')
    x = Symbol('x')
    series = x
    for i in range(2, n+1):
        series = series + (x**i)/i
    pprint(series)
    return series
