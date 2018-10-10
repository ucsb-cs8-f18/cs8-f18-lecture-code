import turtle

def drawRectangle(fred, width, height):
          '''draws a rectangle with the given width and height
          starting at the current location of fred. The turtle fred endup
          at the same position and orientation as it was right before the
          function was called'''
          fred.forward(width)
          fred.left(90)
          fred.forward(height)
          fred.left(90)
          fred.forward(width)
          fred.left(90)
          fred.forward(height)
          fred.left(90)


t = turtle.Turtle()
t.speed(0)
t.shape('turtle')
t.width(8)
t.pencolor('red')
t.left(60)
drawRectangle(t, 50, 100)
t.up()
t.backward(25)
t.left(90)
t.backward(25)
t.right(90)
t.down()
t.pencolor('green')
drawRectangle(t, 100, 150)


