
    
def Period(length, gravity):
    import math
#importing math function
    try:
        period = (2*math.pi)*(math.sqrt(length / gravity))

    except TypeError:
        print("Invalid input(s)")

    except NameError:
        print("Invalid input(s)")   

    print(period)
    return period

#Length(2)
#Gravity(9.81)
Period(1, 9.81)  

