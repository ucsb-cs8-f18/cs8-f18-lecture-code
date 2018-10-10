# lecture3.py
# Diba Mirza
# Silly program

def silly():
                name= input("What is your name? ")
                if len(name)<3:
                                print("Please enter a longer name")
                else:                
                                print("Hi", name + name[-1]*5, "!!!")
                                print("I meant hi", name[0]+name[1]*6 + name[2:])
                                print("Sorry I have a cold", name[2].upper()+name[1:])


def dbl(x):
                return x*2

print(dbl(3))

