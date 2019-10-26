def Length(L):
    try:
        print('Thank you')
    except NameError:
        print('Variable is not defined')
    except ValueError:
        print('Equation cannot be solved')
    

def Gravity(g):
    try:
        print('Thank you')
    except NameError:
        print('Variable is not defined')
    except ValueError:
        print('Equation cannot be solved')
    
def Period():
    import math
    Print((2*math.pi)*(math.sqrt(L/g)))

Length(input())
Gravity(input())
Period()  

