from random import randrange

def diceRoll():
    ''' lab06->return the sum of rolling a one sided die'''
    ''' return the value of one die roll'''
    return randrange(1,7)



def getDistribution(n):
    ''' n is the number of die rolls, return tally'''
    tally = [0]*6
    for i in range(n):
        rv = diceRoll()
        tally[rv-1] = tally[rv-1] +1


    return tally

distribution = getDistribution(200)
print(distribution)

def printDistribution(dist):
    
    

