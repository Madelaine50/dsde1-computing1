def Length():
    print('insert length')
    

def Gravity():
    print('insert gravity' )
    
def Period():
    import math
    Print(2*math.pi)*(math.sqrt(Length(input())/Gravity(input())))

Length(input())
Gravity(input())
Period()  

try:
    print(x)
except NameError:
    print('Variable is not defined')
except ValueError:
    print('Equation cannot be solved')