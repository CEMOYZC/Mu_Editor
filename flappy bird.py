# kutuphanelerimizi import ettik
from pgzhelper import *
import random
import time

# Oyun ekrani ayarlama
WIDTH = 640
HEIGHT = 480

# zemini ekledik.
ground = Actor('ground')
ground.x = 320
ground.y = 460

# kus ekleme
bird = Actor('bird1')
bird.x = 75
bird.y = 100
bird.images = ['bird1', 'bird2', 'bird3', 'bird4']
bird.fps = 10
bird.alive = True  # kus hayatta ise bird.alive = True olacak.


# Game Over oldugunda.
game_over = Actor('game_over')
game_over.x = 320
game_over.y = 200
game_over.scale = 0.2

gravity = 0.3  # Kusun yercekimi
bird.speed = 1

# skor icin
score = 0  # skor

# borulari Ekleyelim. (pipe)
top_pipe = Actor('top')  # ustten gelecek boru
bottom_pipe = Actor('bottom')  # alttan gelecek boru
gap = 100

# borulara konum veriyoruz
top_pipe.x = 640
top_pipe.y = -100

bottom_pipe.x = 640
bottom_pipe.y = top_pipe.height + gap  # bottom_pipe'in yani asagidaki boru y ekseninde top_pipe'a gore konumlandirdik.

pipe_speed = 4  # borularin hizi.

def update():  # ekrandaki hareketleri buradan yapiyoruz.
    global score
    bird.animate()
    bird.y += bird.speed
    bird.speed += gravity
    # borularin ekranda sola dogru hareket etmesi
    top_pipe.x -= pipe_speed
    bottom_pipe.x -= pipe_speed

    # borularin en sona geldiginde tekrar baslangic konumuna gonderip random konumda tekrar sola dogru kaymasi
    if top_pipe.x < - 50:
        offset = random.uniform(-100, -200)
        gap = 150

        top_pipe.midleft = (640, offset)
        bottom_pipe.midleft = (640, offset + top_pipe.height + gap)
        score += 1  # skoru her geciste bir arttiriyoruz.
        sounds.point.play()

    # kusun ekran disina ciktiginda ve yere carptiginda yanmasi.
    if bird.y > HEIGHT - 40 or bird.y < 0:
        bird.alive = False
        bird.image = 'birddead'
        sounds.die.play()

    # kusun borulara carpma ve yanma durumu  colliderect() fonksiyonu carpisma kontrolu yapar.
    if bird.colliderect(top_pipe) or bird.colliderect(bottom_pipe):
        bird.alive = False
        bird.image = 'birddead'
        sounds.hit.play()


def on_mouse_down():
    global score  # yukarida tanimladigimiz score degiskenini fonksiyon icinde kullanabilmek icin basina global yazdik.

    if bird.alive:
        bird.speed = -6.5  # mouse her tikladigimda speed -6.5 olacak
        sounds.wing.play()
    else:
        bird.alive = True  # oyunu yeniden baslatmak icin.
        score = 0


def draw():
    screen.blit('background', (0,0))  # oyun arka plan resmini koyduk.

    # ekranda score'u yazdirma
    screen.draw.text(
        "Score: " + str(score),
        color = 'white',
        midtop = (50, 10),
        scolor = 'black',
        shadow = (0.5, 0.5),
        fontsize = 30
    )

    if bird.alive:
        ground.draw()  # ekledigimiz zemini oyun ekraninda cizdirdik.
        bird.draw()
        top_pipe.draw()
        bottom_pipe.draw()


    else:  # oyuncu yandiysa (kus olduyse)
        time.sleep(1)
        game_over.draw()
        bird.x = 75
        bird.y = 100
        gravity = 0
        bird.speed = 0
        bird.draw()
        screen.draw.text(
            "Click your mouse to play again",
            color = 'white',
            center = (320, 300),
            scolor = 'black',
            shadow = (0.5, 0.5),
            fontsize = 30
        )
        top_pipe.x = 640
        bottom_pipe.x = 640


    # ekranda score'u yazdirma
    screen.draw.text(
        "Score: " + str(score),
        color = 'white',
        midtop = (50, 10),
        scolor = 'black',
        shadow = (0.5, 0.5),
        fontsize = 30
    )






