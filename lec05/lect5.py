def return_dbl( x ):
   return x*2

def print_dbl( x ):
   print(x*2)


def silly( a, b ):
   a = b + 1
   b = a/2
   print(a, ",", b)

def silly_2( a, b ):
   a = b + 1
   b = a/2

def silly_3( a, b ):
   a = b + 1
   b = a/2
   return (a,b)

def mutate( a ):
   a[0] = a[1] + 1
   a[1] = a[0]/2

b = [1, 2, 3]
mutate(b)
print(b)
