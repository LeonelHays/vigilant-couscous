# Turtle program 
# by LeonelHay

import turtle
turtle.color("red")

def main():
  polygon(4, 100)
  back(125)
  polygon(3, 50)

def back(len):
  turtle.peup()
  turtle.backward(len)
  turtle.pendown()

def polygon(num, size):
  for i in range(num):
    turtle.forward(size)
    turtle.left(360 / num)

main()
