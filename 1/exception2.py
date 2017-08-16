from fractions import Fraction

def exception2(number):
    try:
        a = Fraction(number)
        print(a)
    except ZeroDivisionError:
        print('An invalid number')
        raise ZeroDivisionError
