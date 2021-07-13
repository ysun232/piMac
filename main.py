import turtle
#created a turtle.cfg customizable file

#defining the most basic of turtles
wn = turtle.Screen()
sun = turtle.Turtle()
pos = (-150,0) #pair of coordinates to move the turtle before the loop, it draws the line to where it moves
colorTup = (180, 149, 173)
wn.title("Welcome to Sun's turtle! It cleans after itself") #adds a title at the very top of your window
wn.bgcolor("#e8c8c5") #changes the background color

#customizes the screen
#wn.bgpic("landa.jpeg")
wn.screensize(900,600) #reshapes the size of the canvas, you can scroll more to the sides
                        #over writes the turtle.cfg setting

#customizes the turtle
sun.color('red') # this sets both the pen color and the fill color
sun.speed(0) #speed of the turtle, put it to zero if you want fastest
sun.goto(pos) #sets where the turtle will start, drawing a line from where it was supposed to start before
sun.seth(90) #puts the turtle facing north
sun.pensize(5) #changes the size of the lines drawn
sun.penup() #will not draw the lines when moving forward
sun.pencolor('green') #changes the color of the pen
sun.fillcolor('#f68ff7') #changes the color of inside the pen
sun.shape("turtle") #shapes the turtle
sun.resizemode("auto") #resizes the turtle size depending on the pen size
sun.tilt(30) #changes the angle of the turtle without changing the other parameters, it just tilts the turtle

turtle.dot(50, 'green') #draws a dot
turtle.circle(120, 480, 30) #draws a circle using the turtle,
                            #120 means the radius,
                            #480 determines how many circles you will draw(360 = 1 circle)
                            #30 is the number of steps the turtle will take to make the circle

turtle.circle(50) #draws a circle after the half circle
wn.clear() #clears off the circle before drawing the turtle,
            # you will have to change the background color in the cfg if you want it to remain

for steps in range(100):
    sun.stamp() #Stamps the current position of the turtle
    sun.penup() #stops drawing
    print("Is the pen down? ", sun.isdown())
    sun.forward(50)
    print(sun.pos()) #prints out the current position of the turtle
    sun.left(79)
    sun.pendown()
    sun.backward(45) #makes the turtle move back, this time we can see the line drawn since the pen is down
    #with the penup and down, you will only draw the backward moves
    print("Is the pen down? ", sun.isdown())
    #wn.delay(100) #sets a delay in between each iteration so that we can have a better look at it

print("The turtle has stopped moving")
wn.exitonclick() #makes it so that the window does not close by itself

