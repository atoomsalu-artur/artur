import turtle
import random

def joonista_ruut():
    for _ in range(4):
        turtle.forward(60)
        turtle.left(90)

def joonista_ring():
    turtle.circle(40)

def joonista_viisnurk():
    for _ in range(5):
        turtle.forward(60)
        turtle.left(72)

while True:

    kujund = input("Millist kujundit soovid (viisnurk, ring, ruut, suvaline)? ")
    if kujund == "":
        break

    mitu_sisend = input("Mitu kujundit soovid joonistada? ")
    if mitu_sisend == "":
        break

    try:
        mitu = int(mitu_sisend)
    except:
        print("Palun sisesta number!")
        continue

    turtle.speed(0)
    turtle.pensize(2)

    if kujund == "suvaline":

        for _ in range(mitu):
            x = random.randint(-200, 200)
            y = random.randint(-150, 150)

            turtle.penup()
            turtle.goto(x, y)
            turtle.pendown()

            valik = random.choice(["ruut", "ring", "viisnurk"])

            if valik == "ruut":
                joonista_ruut()
            elif valik == "ring":
                joonista_ring()
            elif valik == "viisnurk":
                joonista_viisnurk()

    else:

        turtle.penup()
        turtle.goto(-250, 0)
        turtle.pendown()

        for _ in range(mitu):

            if kujund == "ruut":
                joonista_ruut()
            elif kujund == "ring":
                joonista_ring()
            elif kujund == "viisnurk":
                joonista_viisnurk()
            else:
                print("Tundmatu kujund!")
                break

            turtle.penup()
            turtle.forward(120)
            turtle.pendown()

    j = input("Soovid jätkata? (Enter = lõpetame) ")
    if j == "":
        break
    else:
        turtle.clear()

turtle.done()
