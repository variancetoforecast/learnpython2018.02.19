def DivisionCalc(DivideBy):
    try:
        return 100 / DivideBy
    except ZeroDivisionError:
        print('Error: can not divide by zero dumbo')

DivideBy = input('What would you like to divide by?')
print(DivisionCalc(int(DivideBy)))