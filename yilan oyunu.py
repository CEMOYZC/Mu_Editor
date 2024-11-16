import turtle
import time
import random

# ekran olusturuyoruz
screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)  # ekrani manuel olarak guncellemek icin tracer fonksiyonunu icine sifir gondererek kullandik

delay = 0.1  # saniye cinsinden gecikme suresidir. Yilanin hizini belirtir.
score = 0
high_score = 0
# yilanin kuyruk nesnelerini icerecek bir liste olusturalim
kuyruklar = []

# yilanin kafasini olusturuyoruz.
head = turtle.Turtle()
head.speed(0)
head.color('white')
head.shape('square')
head.penup()
head.goto(0,0)
head.direction = 'stop'

# yiyecigi olusturalim
food = turtle.Turtle()
food.speed(0)
food.color('red')
food.shape('circle')
food.penup()
food.goto(0,100)


# skor tabelasi olusturalim.
pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0, 270)
pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 16, 'bold'))

# Oyunun sonunda eger oyuncu yanarsa ekranda "Game Over" yazacak bir nesne olusturalim.
game_over = turtle.Turtle()
game_over.speed(0)
game_over.color("red")
game_over.penup()
game_over.hideturtle()
game_over.goto(0,0)
game_over.write("", align='center', font=("Courier", 36, 'normal'))

# klavyeden yilani hareket ettirmek icin.
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
        head.sety(head.ycor() +  20)
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

# oyunun ana dongusu
while True:
    # ekran guncelleme
    screen.update()

    # sınır kontrolu - yilan eger duvarlara carparsa oyun biter ve ekranda "Game Over" yazisi gorunecek
    if abs(head.xcor()) > 390 or abs(head.ycor()) > 290:  # duvara carpmis.
        time.sleep(1)  # 1 sn bekletiyoruz
        head.goto(0,0)
        head.direction = 'stop'

        for kuyruk in kuyruklar:
            kuyruk.goto(1000, 1000)  # kuyruklar ekranda gozukmemesi icin ekran disina tasidik.

        kuyruklar.clear()
        score = 0
        pen.clear()
        pen.write(f"Score : {score}  High Score : {high_score}", align="center", font=("Courier", 16, 'normal'))
        game_over.clear()
        game_over.write("GAME OVER", align='center', font=("Courier", 36, 'normal'))  # game over yazisini yazdik.
        time.sleep(2)  # 2 sn ye bekletiyoruz
        game_over.clear()

    # yiyecek ile carpisma
    if head.distance(food) < 20:  # yiyecek ile carpismayi kontrol ediyoruz.
        x = random.randint(-19, 19) * 20
        y = random.randint(-14, 14) * 20
        food.goto(x,y)

        yeni_kuyruk = turtle.Turtle()
        yeni_kuyruk.speed(0)
        yeni_kuyruk.shape("square")
        yeni_kuyruk.color("white")
        yeni_kuyruk.penup()
        kuyruklar.append(yeni_kuyruk)

        # her carptiginda score 10 puan artsin

        score += 10

        # high score'u kontrol edelim
        if score > high_score:
            high_score = score

        pen.clear()
        pen.write(f"Score : {score}  High Score : {high_score}", align="center", font=("Courier", 16, 'normal'))


    # kuyrugu hareket ettirmek
    for i in range(len(kuyruklar) - 1, 0, -1):
        kuyruklar[i].goto(kuyruklar[i-1].xcor(), kuyruklar[i-1].ycor())
    if kuyruklar:
        kuyruklar[0].goto(head.xcor(), head.ycor())

    move()

    # Kuyruk ile Carpisma Kontrolu.
    for kuyruk in kuyruklar:  # sirasi ile tum kuyruklarin carpma kontrolunu yapiyoruz.
        if kuyruk.distance(head) < 20:  # carpisma gerceklesmis demektir.
            time.sleep(1)
            head.goto(0,0)
            head.direction = 'stop'
            for kuyruk in kuyruklar:  # kuyruklari ekrandan uzaklastirark kaldirdik.
                kuyruk.goto(1000, 1000)
            kuyruklar.clear()  # kuyruklar listemizi temizledik.
            score = 0
            pen.clear()
            pen.write(f"Score : {score}  High Score : {high_score}", align="center", font=("Courier", 16, 'normal'))
            game_over.clear()
            game_over.write("GAME OVER", align='center', font=("Courier", 36, 'normal'))  # game over yazisini yazdik.
            time.sleep(2)
            game_over.clear()

    time.sleep(delay)

screen.mainloop()  # oyun dongusunu baslatir. sorunsuz calismasini saglar.

