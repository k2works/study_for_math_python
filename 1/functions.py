# coding=utf-8

'''
0を除く整数aが別の整数bの因数か調べる
'''
def is_factor(a, b):
    if b % a  == 0:
        return True
    else:
        return False

'''
整数の因数を見つける
'''
def factors(b):
    arr = []

    for i in range(1, b+1):
        if b % i == 0:
            print(i)
            arr.append(i)

    return arr
'''
乗算表生成器
'''
def multi_table(a):
    arr = []
    for i in range(1, 11):
        msg = '{0} x {1} = {2}'.format(a, i, a*i)
        print(msg)
        arr.append(msg)

    return arr

'''
単位換算プログラム
'''
def km_miles(arg):
    km = float(arg)
    miles = km / 1.609
    msg = 'Distance in miles: {0}'.format(miles)
    print(msg)
    return miles

def miles_km(arg):
    miles = float(arg)
    km = miles * 1.609
    msg = 'Distance in kilometers: {0}'.format(km)
    print(msg)
    return km

'''
2次方程式求解電卓
'''
def roots(a, b, c):
    arr = []
    D = (b*b - 4*a*c)**0.5
    x_1 = (-b + D)/(2*a)
    x_2 = (-b -D)/(2*a)
    print('x1: {0}'.format(x_1))
    print('x2: {0}'.format(x_2))
    return x_1,x_2
