import turtle
import random

# ekran olusturma
ekran = turtle.Screen()
ekran.setup(width=800, height=600)
ekran.bgcolor('white')
ekran.title('Kaplumbaga Yarisi')

# pist cizimi
def pis_ciz():
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



pis_ciz()

# kirmizi kaplumbağa

kirmizi_kaplumbaga = turtle.Turtle()
kirmizi_kaplumbaga.color('red')
kirmizi_kaplumbaga.shape('turtle')
kirmizi_kaplumbaga.penup()
kirmizi_kaplumbaga.goto(-200, 100)
kirmizi_kaplumbaga.pendown()

#mavi kaplumbağa

mavi_kaplumbaga = turtle.Turtle()
mavi_kaplumbaga.color('blue')
mavi_kaplumbaga.shape('turtle')
mavi_kaplumbaga.penup()
mavi_kaplumbaga.goto(-200, 60)
mavi_kaplumbaga.pendown()



#yeşil kaaplumbağa

yeşil_kaplumbaga = turtle.Turtle()
yeşil_kaplumbaga.color('green')
yeşil_kaplumbaga.shape('turtle')
yeşil_kaplumbaga.penup()
yeşil_kaplumbaga.goto(-200, 20)
yeşil_kaplumbaga.pendown()


#yarisi baslat
def yaris():
    while kirmizi_kaplumbaga.xcor() < 200 and mavi_kaplumbaga.xcor() < 200 and yeşil_kaplumbaga.xcor() < 200 :
        kirmizi_kaplumbaga.forward(random.randint(1, 5))
        mavi_kaplumbaga.forward(random.randint(1, 5))
        yeşil_kaplumbaga.forward(random.randint(1, 5))

yaris()


def kazanan():
    if kirmizi_kaplumbaga.xcor() >=200:
        print('KIRMIZI KAPLUMBAĞA KAZANDI')
    elif mavi_kaplumbaga.xcor() >=200:
        print('MAVİ KAPLUMBAĞA KAZANDI')
    elif yesil_kaplumbaga.xcor() >=200:
        print('YEŞİL KAZANDI')

kazanan()




