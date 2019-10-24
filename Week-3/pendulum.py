def Length(L):
    print('insert length')
    L = input()

def Gravity(g):
    print('insert gravity' )
    g = input()

def Period(T):
    import math
T = (2*math.pi)*(math.sqrt(L/g))
    
try:
    print(x)
except NameError:
    print('Variable is not defined')
except ValueError:
    print('Equation cannot be solved')