import turtle

# Tworzymy okno gry
oknoGry = turtle.Screen()
oknoGry.title("Pong cwiczenie")
oknoGry.bgcolor("black")
oknoGry.setup(width=800, height=600)
oknoGry.tracer(0)

# Lewa rakietka
lewaRakietka = turtle.Turtle()
lewaRakietka.speed(0)
lewaRakietka.shape("square")
lewaRakietka.color("white")
lewaRakietka.shapesize(stretch_wid=5, stretch_len=1)
lewaRakietka.penup()
lewaRakietka.goto(-350, 0)

# Prawa rakietka
prawaRakietka = turtle.Turtle()
prawaRakietka.speed(0)
prawaRakietka.shape("square")
prawaRakietka.color("white")
prawaRakietka.shapesize(stretch_wid=5, stretch_len=1)
prawaRakietka.penup()
prawaRakietka.goto(350, 0)

# Pilka
pilka = turtle.Turtle()
pilka.speed(0)
pilka.shape("circle")
pilka.color("white")
pilka.penup()
pilka.goto(0, 0)
pilka.dx = 0.2
pilka.dy = 0.2

# Funkcje
def lewaRakietka_up():
    y = lewaRakietka.ycor()
    y += 20
    lewaRakietka.sety(y)

def lewaRakietka_down():
    y = lewaRakietka.ycor()
    y -= 20
    lewaRakietka.sety(y)

def prawaRakietka_up():
    y = prawaRakietka.ycor()
    y += 20
    prawaRakietka.sety(y)

def prawaRakietka_down():
    y = prawaRakietka.ycor()
    y -= 20
    prawaRakietka.sety(y)
    
# Klawisze obslugi
oknoGry.listen()
oknoGry.onkeypress(lewaRakietka_up, "w")
oknoGry.onkeypress(lewaRakietka_down, "s")
oknoGry.onkeypress(prawaRakietka_up, "8")
oknoGry.onkeypress(prawaRakietka_down, "5")

# Petla gry
while True:
    oknoGry.update()
    
    # Poruszanie pilki
    pilka.setx(pilka.xcor() + pilka.dx)
    pilka.sety(pilka.ycor() + pilka.dy)
    
    # Sprawdzanie kolizji z krawedziami
    if pilka.ycor() > 290:
        pilka.sety(290)
        pilka.dy *= -1

    if pilka.ycor() < -290:
        pilka.sety(-290)
        pilka.dy *= -1

    if pilka.xcor() > 390:
        pilka.goto(0, 0)
        pilka.dx *= -1

    if pilka.xcor() < -390:
        pilka.goto(0, 0)
        pilka.dx *= -1

    # Sprawdzanie kolizji z rakietkami
    if pilka.xcor() > 340 and pilka.xcor() < 350 and (pilka.ycor() < prawaRakietka.ycor() +40 and pilka.ycor() > prawaRakietka.ycor() -40):
        pilka.setx(340)
        pilka.dx *= -1
    if pilka.xcor() < -340 and pilka.xcor() > -350 and (pilka.ycor() < lewaRakietka.ycor() +40 and pilka.ycor() > lewaRakietka.ycor() -40):
        pilka.setx(-340)
        pilka.dx *= -1
