#imported turtle module
import turtle


wind = turtle.Screen() #intialize screen
wind.title('Ping Pong By Qais') #set the tile of the window
wind.bgcolor('black') #set background color of the window
wind.setup(width=800,height=600) #set the width and height of the window
wind.tracer(0) #stops the windwo from updating automatically


#bat1
bat1 = turtle.Turtle() #intialize turtle object(shape)
bat1.speed(0) #speed of the animation
bat1.shape('square') #sahpe of the object
bat1.shapesize(stretch_wid=5, stretch_len=1) #stretches the shape to meet the size
bat1.color('blue')
bat1.penup() #stop the object from drawing lines
bat1.goto(-350, 0) #set position of the object
#bat2
bat2 = turtle.Turtle()
bat2.speed(0)
bat2.shape('square')
bat2.shapesize(stretch_wid=5, stretch_len=1)
bat2.color('red')
bat2.penup()
bat2.goto(350, 0)
#ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape('square')
ball.color('white')
ball.penup()
ball.goto(0, 0)
ball.dx = 0.2
ball.dy = 0.2

#score
score1 = 0
score2 = 0
score = turtle.Turtle()
score.speed (0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0, 260)
score.write("Player 1: 0 Player 2: 0", align="center", font=('Courier',24,'normal'))



#functions
def bat1_up():
    y = bat1.ycor() #get the y coodrinate of the object
    y += 20  #set y to increase by 20
    bat1.sety(y)  #set the y of the object to the new y

def bat1_down():
    y = bat1.ycor()
    y -= 20  #set y to decrease by 20
    bat1.sety(y)   

def bat2_up():
    y = bat2.ycor()
    y += 20
    bat2.sety(y)

def bat2_down():
    y = bat2.ycor()
    y -= 20
    bat2.sety(y)     

#keyboard bindings
wind.listen()  #tell window to expect keyboard input
wind.onkeypress(bat1_up, 'w')    #when pressin the key assinged the function object is invoked
wind.onkeypress(bat1_down, 's')
wind.onkeypress(bat2_up, 'Up')    
wind.onkeypress(bat2_down, 'Down')


#main game loop
while True:
    wind.update() #updates thw screen everytime the loop runs

    #move th e ball
    ball.setx(ball.xcor() + ball.dx ) #ball starts at 0 and everytime loops run--->+0.2 xaxis
    ball.sety(ball.ycor() + ball.dy ) #ball starts at 0 and everytime loops run--->+0.2 yaxis


    #border check , top border +300px, bottom border -300px, ball is 20px
    if ball.ycor() > 290: #if ball is at top border
        ball.sety(290) #set y coordinate +290
        ball.dy *= -1  #reverse direction, making +0.2--->-0.2
        

    if ball.ycor() < -290: #if ball is at bottom border
        ball.sety(-290)
        ball.dy *= -1
        

    if ball.xcor() > 390: #if ball is at right border
        ball.goto(0, 0) #return ball to center
        ball.dx *= -1 #reverse the x direction
        score1 += 1
        score.clear()
        score.write("Player 1: {} Player 2: {}".format(score1, score2), align="center", font=('Courier',24,'normal'))


    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score2 += 1
        score.clear()
        score.write("Player 1: {} Player 2: {}".format(score1, score2), align="center", font=('Courier',24,'normal'))    
    
    #colusion bat and ball
    if (ball.xcor () > 340 and ball.xcor() < 350) and (ball.ycor() < bat2.ycor() + 40 and ball.ycor() > bat2.ycor() - 40):
       ball.setx(340)
       ball.dx *= -1
       

    if (ball.xcor () < -340 and ball.xcor() > -350) and (ball.ycor() < bat1.ycor() + 40 and ball.ycor() > bat1.ycor() - 40):
       ball.setx(-340)
       ball.dx *= -1 
       
  