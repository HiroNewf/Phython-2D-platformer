import turtle
import keyboard
import time

# Screen
wn = turtle.Screen()
wn.title("My Screen")
wn.bgcolor("Light Blue")
wn.setup(width=1920, height=1080)
wn.tracer(0)

# Player
player = turtle.Turtle()
player.speed(10)
player.shape("square")
player.color("white")
player.penup()
player.goto(-850, -450)

#Floor
floor = turtle.Turtle()
floor.hideturtle()
floor.penup()
floor.goto(-1000, -470)
floor.width(20)
floor.color("black")
floor.pendown()
floor.forward(2000)

# Main game loop
while True:
    wn.update()

    try:
        if keyboard.is_pressed('d'):
            x = player.xcor()
            x += 0.45
            player.setx(x)
        if keyboard.is_pressed('a'):
            x = player.xcor()
            x -= 0.45
            player.setx(x)
        if keyboard.is_pressed('space'):
            y = player.ycor()
            y += 1
            player.sety(y)
    finally:
        if player.ycor() > -450:
            y = player.ycor()
            y -= 0.5
            player.sety(y)
