def exception3(number):
    try:
        a = complex(number)
        print(a)
    except ZeroDivisionError:
        print('An invalid number')
        raise ZeroDivisionError
