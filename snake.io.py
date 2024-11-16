Cemalettin Yazıcı
cyzc.
Çevrim içi

Murat - Instructor — 01.08.2024 12:22
# pist cizimi
def pist_ciz():
    cizici = turtle.Turtle()  # Yeni bir nesne olusturduk. bu bizim icin pisti cizecek.
    cizici.speed(0)  # Olusturdugumuz cizici nesnesinin hizini belirledik. Ve maksimum yaptik.
    cizici.penup()  # kalemi kaldirdi.

    # pist cizimi
    # kirmizi_kaplumbaganin yolu
    cizici.goto(-200, 100)  # baslangic pozisyonuna gonderdik
    cizici.pendown()  # kalemi indirdik
    cizici.color('red')  # kalemin rengi.
    cizici.forward(400)  # 400 px'lik bir yol cizdirdik.(saga dogru)

    # mavi_kaplumbaganin yolu
    cizici.penup()
    cizici.goto(-200, 60)  # baslangic pozisyonuna gonderdik
    cizici.pendown()  # kalemi indirdik
    cizici.color('blue')  # kalemin rengi.
    cizici.forward(400)  # 400 px'lik bir yol cizdirdik.(saga dogru)

    # yesil_kaplumbaganin yolu
    cizici.penup()
    cizici.goto(-200, 20)  # baslangic pozisyonuna gonderdik
    cizici.pendown()  # kalemi indirdik
    cizici.color('green')  # kalemin rengi.
    cizici.forward(400)  # 400 px'lik bir yol cizdirdik.(saga dogru)

    # FINISH CIZGISI
    cizici.penup()
    cizici.goto(200, 140)
    cizici.pendown()
    cizici.color('black')
    cizici.right(90)
    cizici.forward(160)



    cizici.penup()
    cizici.goto(200, 160)
    cizici.write('FINISH', align='center', font=('Arial', 16, 'bold'))

    cizici.hideturtle()  # cizici'yi gizledik



pist_ciz()
Ömer Karan Bülbül — 01.08.2024 12:27
Görsel
Murat - Instructor — 01.08.2024 12:38
# yarisi baslat
def yaris():
    while kirmizi_kaplumbaga.xcor() < 200 and mavi_kaplumbaga.xcor() < 200 and yesil_kaplumbaga.xcor() < 200:
        kirmizi_kaplumbaga.forward(random.randint(1, 5))
        mavi_kaplumbaga.forward(random.randint(1, 5))
        yesil_kaplumbaga.forward(random.randint(1, 5))

yaris()
# kazanani belirleyelim
def kazanan():
    if kirmizi_kaplumbaga.xcor() >= 200:
        print('KIRMIZI KAPLUMBAGA KAZANDI!!!')
    elif mavi_kaplumbaga.xcor() >= 200:
        print("MAVI KAPLUMBAGA KAZANDI!!!")
    elif yesil_kaplumbaga.xcor() >= 200:
        print("YESIL KAPLUMBAGA KAZANDI")


kazanan()
Murat - Instructor — 01.08.2024 12:46
Görsel
# TODO
# ekran.clear()
# yeni kazanani yazacak bir nesne olusturalim(isci)
# write ile kazananani yazsin (rengi beyaz olsun)
# ekranin arka plan rengide kazanan kaplumbaga renginde olsun.
import turtle
import random

# ekran olusturma
ekran = turtle.Screen()
ekran.setup(width=800, height=600)
ekran.bgcolor('white')
ekran.title('Kaplumbaga Yarisi')

# pist cizimi
def pist_ciz():
    cizici = turtle.Turtle()  # Yeni bir nesne olusturduk. bu bizim icin pisti cizecek.
    cizici.speed(0)  # Olusturdugumuz cizici nesnesinin hizini belirledik. Ve maksimum yaptik.
    cizici.penup()  # kalemi kaldirdi.

    # pist cizimi
    # kirmizi_kaplumbaganin yolu
    cizici.goto(-200, 100)  # baslangic pozisyonuna gonderdik
    cizici.pendown()  # kalemi indirdik
    cizici.color('red')  # kalemin rengi.
    cizici.forward(400)  # 400 px'lik bir yol cizdirdik.(saga dogru)

    # mavi_kaplumbaganin yolu
    cizici.penup()
    cizici.goto(-200, 60)  # baslangic pozisyonuna gonderdik
    cizici.pendown()  # kalemi indirdik
    cizici.color('blue')  # kalemin rengi.
    cizici.forward(400)  # 400 px'lik bir yol cizdirdik.(saga dogru)

    # yesil_kaplumbaganin yolu
    cizici.penup()
    cizici.goto(-200, 20)  # baslangic pozisyonuna gonderdik
    cizici.pendown()  # kalemi indirdik
    cizici.color('green')  # kalemin rengi.
    cizici.forward(400)  # 400 px'lik bir yol cizdirdik.(saga dogru)

    # FINISH CIZGISI
    cizici.penup()
    cizici.goto(200, 140)
    cizici.pendown()
    cizici.color('black')
    cizici.right(90)
    cizici.forward(160)



    cizici.penup()
    cizici.goto(200, 160)
    cizici.write('FINISH', align='center', font=('Arial', 16, 'bold'))

    cizici.hideturtle()  # cizici'yi gizledik



pist_ciz()
# kaplumbagalari olusturalim

# kirmizi_kaplumbaga

kirmizi_kaplumbaga = turtle.Turtle()  # bir kaplumbaga nesnesi olusturduk.
kirmizi_kaplumbaga.color('red')  # rengini kirmizi yaptik
kirmizi_kaplumbaga.shape('turtle')  # kaplumbaga sekli verdik
kirmizi_kaplumbaga.penup()  # kalemi kaldirdim
kirmizi_kaplumbaga.goto(-200, 100)
kirmizi_kaplumbaga.pendown()  # pisti zaten cizdigimiz icin istege bagli yazilabilir.


# mavi_kaplumbaga
mavi_kaplumbaga = turtle.Turtle()  # bir kaplumbaga nesnesi olusturduk.
mavi_kaplumbaga.color('blue')  # rengini mavi yaptik
mavi_kaplumbaga.shape('turtle')  # kaplumbaga sekli verdik
mavi_kaplumbaga.penup()  # kalemi kaldirdim
mavi_kaplumbaga.goto(-200, 60)
mavi_kaplumbaga.pendown()  # pisti zaten cizdigimiz icin istege bagli yazilabilir.

# yesil_kaplumbaga
yesil_kaplumbaga = turtle.Turtle()  # bir kaplumbaga nesnesi olusturduk.
yesil_kaplumbaga.color('green')  # rengini yesil yaptik
yesil_kaplumbaga.shape('turtle')  # kaplumbaga sekli verdik
yesil_kaplumbaga.penup()  # kalemi kaldirdim
yesil_kaplumbaga.goto(-200, 20)
yesil_kaplumbaga.pendown()  # pisti zaten cizdigimiz icin istege bagli yazilabilir.

# yarisi baslat
def yaris():
    while kirmizi_kaplumbaga.xcor() < 200 and mavi_kaplumbaga.xcor() < 200 and yesil_kaplumbaga.xcor() < 200:
        kirmizi_kaplumbaga.forward(random.randint(1, 5))
        mavi_kaplumbaga.forward(random.randint(1, 5))
        yesil_kaplumbaga.forward(random.randint(1, 5))

yaris()
# kazanani belirleyelim
def kazanan():
    if kirmizi_kaplumbaga.xcor() >= 200:
        print('KIRMIZI KAPLUMBAGA KAZANDI!!!')
    elif mavi_kaplumbaga.xcor() >= 200:
        print("MAVI KAPLUMBAGA KAZANDI!!!")
    elif yesil_kaplumbaga.xcor() >= 200:
        print("YESIL KAPLUMBAGA KAZANDI")


kazanan()

# TODO
# ekran.clear()
# yeni kazanani yazacak bir nesne olusturalim(isci)
# write ile kazananani yazsin (rengi beyaz olsun)
# ekranin arka plan rengide kazanan kaplumbaga renginde olsun.
# chatgpt den yardim alabilirsiniz.
Murat - Instructor — 03.08.2024 10:46
@everyone

Arkadaslar Herkese Gunaydinlar!!
Derse hazirmisiniz? Bu derste sizlerle yilan oyunu kodlayacagiz.
Ders 15
Ders15
Saturday, August 3 · 11:00am – 1:00pm
Time zone: Europe/Istanbul
Google Meet joining info
Video call link: https://meet.google.com/dbz-gyfq-trp
Or dial: ‪(GB) +44 20 3937 4544‬ PIN: ‪633 428 559‬#
More phone numbers: https://tel.meet/dbz-gyfq-trp?pin=5515075854441

Join this video meeting
Real-time meetings by Google. Using your browser, share your video, desktop, and presentations with teammates and customers.
Görsel
Murat - Instructor — 03.08.2024 11:04
@everyone Bekliyoruz arkadaslar basladik
Murat - Instructor — 03.08.2024 11:35
# kazanani belirleyelim
def kazanan():
    kazanan_kaplumbaga = ''
    kazanan_renk = ''

    if kirmizi_kaplumbaga.xcor() >= 200:
        kazanan_kaplumbaga = 'KIRMIZI KAPLUMBAGA KAZANDI!!!'
        kazanan_renk = 'red'
    elif mavi_kaplumbaga.xcor() >= 200:
        kazanan_kaplumbaga = "MAVI KAPLUMBAGA KAZANDI!!!"
        kazanan_renk = 'blue'
    elif yesil_kaplumbaga.xcor() >= 200:
        kazanan_kaplumbaga = "YESIL KAPLUMBAGA KAZANDI"
        kazanan_renk = 'green'

    ekran.clear()
    ekran.bgcolor(kazanan_renk)

    cizici_kazanan = turtle.Turtle()
    cizici_kazanan.speed(0)
    cizici_kazanan.color('white')
    cizici_kazanan.penup()
    cizici_kazanan.goto(0,100)
    cizici_kazanan.write(kazanan_kaplumbaga, align='center', font= ('Arial', 36, 'bold'))
    cizici_kazanan.hideturtle()
Ömer Karan Bülbül — 03.08.2024 11:40
Görsel
Murat - Instructor — 03.08.2024 11:47
import turtle
import time
import random

# ekran olusturuyoruz
screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)  # ekrani manuel olarak guncellemek icin tracer fonksiyonunu icine sifir gondererek kullandik

# yilanin kafasini olusturuyoruz.
head = turtle.Turtle()
head.speed(0)
head.color('white')
head.shape('square')
head.penup()
head.goto(0,0)
head.direction = 'stop'

screen.update()
delay = 0.1  # saniye cinsinden gecikme suresidir.
score = 0
high_score = 0
import turtle
import time
import random

# ekran olusturuyoruz
screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)  # ekrani manuel olarak guncellemek icin tracer fonksiyonunu icine sifir gondererek kullandik

delay = 0.1  # saniye cinsinden gecikme suresidir.
score = 0
high_score = 0


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


screen.update()
Mesutbahadır — 03.08.2024 12:11
Görsel
Murat - Instructor — 03.08.2024 12:13
# yilanin kuyruk nesnelerini icerecek bir liste olusturalim
kuyruklar = []

# skor tabelasi olusturalim.
pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0, 270)
pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 16, 'bold'))
import turtle
import time
import random

# ekran olusturuyoruz
screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)  # ekrani manuel olarak guncellemek icin tracer fonksiyonunu icine sifir gondererek kullandik

delay = 0.1  # saniye cinsinden gecikme suresidir.
score = 0
high_score = 0


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

# yilanin kuyruk nesnelerini icerecek bir liste olusturalim
kuyruklar = []

# skor tabelasi olusturalim.
pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0, 270)
pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 16, 'bold'))

screen.update()
Mesutbahadır — 03.08.2024 12:18
Görsel
Murat - Instructor — 03.08.2024 12:21
# Oyunun sonunda eger oyuncu yanarsa ekranda "Game Over" yazacak bir nesne olusturalim.
game_over = turtle.Turtle()
game_over.speed(0)
game_over.color("red")
game_over.penup()
game_over.hideturtle()
game_over.goto(0,0)
game_over.write("", align='center', font=("Courier", 36, 'normal'))
Murat - Instructor — 03.08.2024 12:34
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
    kaplumbaga.sety(kaplumbaga.ycor() +20)
def go_down():
    kaplumbaga.sety(kaplumbaga.ycor() -20)
def go_right():
    kaplumbaga.setx(kaplumbaga.xcor() +20)
def go_left():
    kaplumbaga.setx(kaplumbaga.xcor() -20)

ekran.onkey(go_up, "w")
ekran.onkey(go_down, "s")
ekran.onkey(go_right, "d")
ekran.onkey(go_left, "a")
Murat - Instructor — 03.08.2024 12:53
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
Mesutbahadır — 06.08.2024 10:45
Hocam katılma isteyimi onaylamıyorsunuz
Yasin — 06.08.2024 10:47
Ders 11 de baslayacak ya Mesut Bahadir, o zaman biz de meet e girecegiz. o zaman butun ogrencileri onaylayacagiz
Mesutbahadır — 06.08.2024 10:47
tamam
Murat - Instructor — 06.08.2024 11:07
Görsel
Görsel
Görsel
Murat - Instructor — 06.08.2024 11:16
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
Mesutbahadır — 06.08.2024 11:44
Görsel
Murat - Instructor — 06.08.2024 11:45
# oyunun ana dongusu
while True:
    # ekran guncelleme
    screen.update()

    # sınır kontrolu - yilan eger duvarlara carparsa oyun biter ve ekranda "Game Over" yazisi gorunecek
import turtle
import time
import random

# ekran olusturuyoruz
screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)  # ekrani manuel olarak guncellemek icin tracer fonksiyonunu icine sifir gondererek kullandik

delay = 0.1  # saniye cinsinden gecikme suresidir.
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

Ömer Karan Bülbül — 06.08.2024 11:51
Görsel
calismiiyor
Murat - Instructor — 06.08.2024 11:53
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
Murat - Instructor — 06.08.2024 12:09
Görsel
Murat - Instructor — 06.08.2024 12:20
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
        pen.write(f"Score {score}  High Score : {high_score}", align="center", font=("Courier", 36, 'normal'))
        game_over.clear()
        game_over.write("GAME OVER", align='center', font=("Courier", 36, 'normal'))  # game over yazisini yazdik.
        time.sleep(2)  # 2 sn ye bekletiyoruz
        game_over.clear()

        # yiyecek ile carpisma
Murat - Instructor — 06.08.2024 12:41
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
        pen.write(f"Score {score}  High Score : {high_score}", align="center", font=("Courier", 36, 'normal'))
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
        pen.write(f"Score {score}  High Score : {high_score}", align="center", font=("Courier", 36, 'normal'))
Mesutbahadır — 06.08.2024 12:44
Görsel
Murat - Instructor — 06.08.2024 12:55
import turtle
import time
import random

# ekran olusturuyoruz
screen = turtle.Screen()
Genişlet

genc_fikir_yilan_oyunu_turtle.py
4 KB


Görsel
Murat - Instructor — bugün saat 10:56
@everyone
Ders 17
Thursday, August 8 · 11:00am – 1:00pm
Time zone: Europe/Istanbul
Google Meet joining info
Video call link: https://meet.google.com/qhu-povm-nst
Or dial: ‪(GB) +44 20 3956 0185‬ PIN: ‪806 064 067‬#
More phone numbers: https://tel.meet/qhu-povm-nst?pin=3379190038046

Join this video meeting
Real-time meetings by Google. Using your browser, share your video, desktop, and presentations with teammates and customers.
Görsel
Buyrun arkadaslar
Linke tiklayip derse katilabilirsiniz.
Murat - Instructor — bugün saat 11:06
Görsel
Görsel
Görsel
Murat - Instructor — bugün saat 11:24
import turtle
import time
import random

# ekran olusturuyoruz
screen = turtle.Screen()
Genişlet

genc_fikir_yilan_oyunu_turtle.py
5 KB



﻿
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



















