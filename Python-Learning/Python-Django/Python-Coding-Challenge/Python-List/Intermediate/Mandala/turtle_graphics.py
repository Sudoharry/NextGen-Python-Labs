"""
    This program draws a beautiful mandala-like pattern using turtle — a built-in graphics module in Python.
"""
import turtle
import colorsys

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("black")
t.speed(0)
n = 36
h = 0

for i in range(360):
    c = colorsys.hsv_to_rgb(h, 1, 1)
    t.color(c)
    t.forward(i * 3 / n + i)
    t.left(59)
    t.forward(i * 3 / n + i)
    t.left(59)
    t.forward(i * 3 / n + i)
    t.left(59)
    t.left(1)
    h += 0.005

turtle.done()
