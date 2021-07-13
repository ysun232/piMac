import turtle

wn = turtle.Screen()
sun = turtle.Turtle()
sun.speed(0)

userNum = input("Please input 10 if you want to see a turtle move in a circle, anything else to see a square")

if userNum == "10": #will print a circle because of a repitition of 100 times of rhte forward and left 65
    for sunT in range(100):
        sun.forward(100)
        sun.stamp()
        sun.left(65)
    wn.exitonclick()
else:
    if userNum == "hidden": #entering hidden will draw a square
        for sunT in range(4):
            sun.forward(150)
            sun.left(90)
    else:
        for sunT in range(3): #entering anything else will draw a triangle
            sun.forward(150)
            sun.left(120)

    wn.exitonclick()
