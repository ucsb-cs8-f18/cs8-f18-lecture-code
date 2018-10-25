def isInteger(x):
    ''' return True if x is an integer otherwise return False'''
    return type(x) == int

def isNegative(x):
    ''' Assume x is an integer, return True if x is negative,
    otherwise return False'''
    
    return x < 0

def isNegativeAwesome(x):
    ''' return True if x is negative,
    otherwise return False'''
    if type(x) == int:
        return x < 0
    else:
        return False

def isNegativeBoolExp(x):
    ''' return True if x is negative,
    otherwise return False'''
    return  type(x) == int and x < 0
    
