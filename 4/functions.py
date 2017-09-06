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

def print_series2(n, x_value):

    # 出力を逆順に初期化
    init_printing(order='rev-lex')
    x = Symbol('x')
    series = x
    for i in range(2, n+1):
        series = series + (x**i)/i
    pprint(series)

    # x_valueで級数評価
    series_value = series.subs({x:x_value})
    print('Value of the series at {0}: {1}'.format(x_value, series_value))
    return series_value

'''
２式の積
'''

from sympy import expand, sympify
from sympy.core.sympify import SympifyError

def product(expr1, expr2):
    try:
        expr1 = sympify(expr1)
        expr2 = sympify(expr2)
    except SympifyError:
        print('Invalid input')
    else:
        prod = expand(expr1*expr2)
        print(prod)
        return prod
