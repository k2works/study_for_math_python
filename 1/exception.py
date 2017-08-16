def exception(number):
    try:
        a = float(number)
        print(a)
    except ValueError:
        print('An invalid number')
        raise ValueError
