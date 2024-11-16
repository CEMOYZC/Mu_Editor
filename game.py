import turtle

ekran = turtle.Screen()
ekran.setup(width=800, height=600)
ekran.bgcolor('black')


kaplumbaga = turtle.Turtle()
kaplumbaga.shape('turtle')
kaplumbaga.color('white')
kaplumbaga.penup()
kaplumbaga.goto(0,0)



ekran.listen()
def go_up():
    kaplumbaga.setheading(90)  # kuzey yonu 90  - north
    kaplumbaga.forward(20)
def go_down():
    kaplumbaga.setheading(270)  # guney yonu 270  -  south
    kaplumbaga.forward(20)
def go_right():
    kaplumbaga.setheading(0)  # dogu yonu 0  - east
    kaplumbaga.forward(20)
def go_left():
    kaplumbaga.setheading(180)  # bati yonu  180  -  west
    kaplumbaga.forward(20)

ekran.onkey(go_up, "Up")
ekran.onkey(go_down, "Down")
ekran.onkey(go_right, "Right")
ekran.onkey(go_left, "Left")
