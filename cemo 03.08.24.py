import turtle
import time
import random

#ekran oluşturma
screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('snake game')
screen.tracer(0)

delay = 0.1 #saniye cinsinden gecikme süresidir
score = 0
high_score = 0


#yilanın kafasını oluşturuyoruz
head = turtle.Turtle()
head.speed(0)
head.color('white')
head.shape('square')
head.penup()
head.goto(0, 0)
head.direction = 'stop'

# yiyeceği oluşturalım,
food = turtle.Turtle()
food.speed(0)
food.color('red')
food.shape('circle')
food.penup()
food.goto(0, 100)

# yılanın kuyruklarını oluşturma
kuyruklar = []

#skor tabelası oluşturalım
pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0, 270)
pen.write("Score: 0 High score: 0", align="center", font=("Courier", 16, 'bold'))

# oyunun sonunde eğer oyuncu yanarsa game ouar oluştuer

game_over = turtle.Turtle()
game_over.speed(0)
game_over.color('red')
game_over.penup()
game_over.hideturtle()
game_over.goto(0,0)
game_over.write("", align='center', font=("Courier", 36, 'normal'))

def go_up():
    if head.direction != "down":
        head.direction = "up"
def go_down():
    if head.direction != "up":
        head.direction = "down"
def go_right():
    if head.direction != "left":
        head.direction = "right"
def go_left():
    if head.direction != "right":
        head.direction = "left"

def move():
    if head.direction == "up":
        head.sety(head.ycor() + 20)
    if head.direction == "down":
        head.sety(head.ycor() - 20)
    if head.direction == "right":
        head.setx(head.xcor() + 20)
    if head.direction == "left":
        head.setx(head.xcor() - 20)


screen.listen()
screen.onkey(go_up, 'w')
screen.onkey(go_down, 's')
screen.onkey(go_right, 'd')
screen.onkey(go_left, 'a')

#oyunun ana döngüsü
while True:
    #ekran güncelleme
    screen.update()

    #sınır kontrolü- yılan eger duvarlara carparsa game over gorunecek
    if abs(head.xcor()) > 390 or abs(head.ycor()) > 290:
        time.sleep(1) # 1 sn bekle
        head.goto(0,0)
        head.direction = 'stop'

        for kuyruk in kuyruklar:
            kuyruklar.goto(1000, 1000) #kuyruklar ekranda gözükmemesi için

        kuyruklar.clear()
        score = 0
        pen.clear()
        pen.write(f"Score {score} High Score : {high_score}", align="center", font = ("Courier", 36, 'normal'))
        game_over.clear()
        game_over.write("GAME OVER", align='center', font=("Courier", 36, 'normal'))
        time.sleep(2)
        game_over.clear()

    # yiyecek ile çarpışma
    if head.distance(food) < 20: # yiyecek ile çarpışmayı kontrol ediyoruz
        x = random.randint(-19, 19) * 20
        y = random.randit(-14, 14) * 20
        food.goto(x,y)

        yeni_kuyruk = turtle.Turtle()
        yeni_kuyruk.speed(0)
        yeni_kuyruk.shape("square")
        yeni_kuyruk.color("white")
        yeni_kuyruk.penup()
        yeni_kuyruk.append(yeni_kuyruk)

        # her çarptığında skor 10 artsın

        score += 10

        # high scoru ayarla
        if score > high_score:
            high_score = score

        pen.clear()
        pen.write(f"Score {score}  High Score : {high_score}", align="center", font=("Courier", 36, 'normal'))


    # kuyruğu hareket ettirmek
    for i in range(len(kuyruklar) -1, 0, -1):
        kuyruklar[i].goto(kuyruklar[i-1].xcor(), kuyruklar[i-1].ycor())
    if kuyruklar:
    kuyruklar[0].goto(head.xcor(), head.ycor())

    move()








