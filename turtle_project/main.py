import turtle
import colorsys

# Drawing the stem
turtle.speed("fastest")
turtle.penup()
turtle.goto(0, -350)
turtle.pendown()
turtle.pensize(20)
turtle.pencolor('green')
turtle.setheading(90)
turtle.goto(0, 0)
turtle.pensize(1)

# Drawing the petals
hue = 0.0
for i in range(194):
    turtle.circle(190-i, 90)
    color = colorsys.hsv_to_rgb(hue, 1, 1)
    turtle.pencolor(color)
    turtle.left(90)
    turtle.circle(190-i, 90)
    turtle.left(18)
    hue += 0.01

turtle.hideturtle()

turtle.mainloop()

