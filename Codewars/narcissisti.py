import math

def narcissistic( value ):
    power = len(str(value))
    sum = 0
    for x in str(value):
        sum+=math.pow(int(x), power)
        print(int(sum))
    if sum == value:
        return True
    else:
        return False


narcissistic(123)