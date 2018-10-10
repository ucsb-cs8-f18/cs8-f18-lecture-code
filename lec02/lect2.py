import turtle

def Rectangle_1(t, width, height):
   t.begin_fill()
   t.forward(width)
   t.left(90)
   t.forward(height)
   t.left(90)
   t.forward(width)
   t.left(90)
   t.forward(height)
   t.left(90)
   t.end_fill()
   


jane = turtle.Turtle()
chris = turtle.Turtle()
chris.width(8)
jane.clear()
jane.shape("turtle")
jane.speed(0)
jane.width(8)
jane.color("red","yellow")
Rectangle_1(chris, 50, 100)
jane.up()
jane.goto(-100,0)
jane.down()
jane.seth(60)
Rectangle_1(jane, 10, 200)




    
