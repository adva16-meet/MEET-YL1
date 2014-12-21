import turtle
turtle.penup()
turtle.goto(-250,250)
turtle.pendown()
turtle.goto(-250,-250)
turtle.goto(250,-250)
turtle.goto(250,250)
turtle.goto(-250,250)
turtle.penup()
turtle.goto(-250,200)
turtle.pendown()
turtle.goto(250,200)
turtle.penup()
turtle.goto(6,250)
turtle.pendown()
turtle.goto(6,200)
turtle.penup()
turtle.goto(0,0)

blue = turtle.Turtle()
blue.pu()
blue.shape("square")
blue.shapesize(4,12,1)
blue.color("blue")
blue.goto(125,225)
#turtle.color('blue')
#turtle.begin_fill()
#turtle.pendown()
#turtle.goto(6,250)
#turtle.goto(250,250)
#turtle.goto(250,200)
#turtle.goto(6,200)
#turtle.penup()
#turtle.end_fill()


pink = turtle.Turtle()
pink.pu()
pink.shape("square")
pink.shapesize(4,12,1)
pink.color("pink")
pink.goto(-100,225)
##turtle.color('pink')
##turtle.begin_fill()
##turtle.pendown()
##turtle.goto(6,250)
##turtle.goto(-250,250)
##turtle.goto(-250,200)
##turtle.goto(6,200)
##turtle.penup()
##turtle.end_fill()

def  brush_1_circle(x,y):
     turtle.begin_fill()
     turtle.fillcolor('red')
     turtle.penup()
     turtle.goto(x,y)
     turtle.pendown
##     turtle.Pen(x+50,y+50)
     turtle.goto(x,y+50)
     turtle.goto(x,y)
     turtle.end_fill

turtle.onclick(brush_1_circle,1,add=True)
turtle.onscreenclick(brush_1_circle,btn=3,add=True)
 

 



	
def changetoblue(x,y):
     turtle.pencolor("blue")
def changetopink(x,y):
     turtle.pencolor("pink")
blue.onclick(changetoblue)
pink.onclick(changetopink)
turtle.speed(0)
turtle.shape("circle")
turtle.pensize(10)
turtle.color('pink','red')
turtle.pendown()
turtle.ondrag(turtle.goto, btn=1, add=None)



turtle.mainloop()
              
