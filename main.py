#day 4 to use loops as a function for multiple uses but various paramenters (sizes)
#
import turtle
turtle.color("blue")
#
def polygon(num, size):
  for i in range(num):
      turtle.forward(size)
      turtle.left(360 / num)

#forward helper function
def move(len):
  back(-1 * len)

def back(len):
  turtle.penup()
  turtle.backward(len)
  turtle.pendown()
  
def spiral(len, angle):
  for i in range(len, 5, -5):
    turtle.forward(i)
    turtle.right(angle)
    
spiral(75, 45)
move(150)
turtle.color("red")


#for n in range(3, 10):
 # move(50)
#  polygon(n, 100 / n)
#  back(50)
#  turtle.right(360 / 7)
