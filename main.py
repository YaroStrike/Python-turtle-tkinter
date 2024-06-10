import turtle
import tkinter as tk
from tkinter import *
from tkinter import ttk

screen = turtle.Screen()
screen.title("Turtle Graphics with Tkinter")

t = turtle.Turtle()
t.speed(0)
t.penup()
t.goto(-500, 0)
t.pendown()
t.goto(500, 0)
t.penup()
t.goto(0, -500)
t.pendown()
t.goto(0, 500)

def draw_circles():
    draw_button.destroy()
    global R1, R2
    R1 = float(entry_r1.get())
    R2 = float(entry_r2.get())
    tsh = float(R1 - R2)
    rng = float(R2/6)
    
    t.penup()
    t.goto(0, -R1)
    t.pendown()
    t.circle(R1)
    
    t.penup()
    t.goto(0, -R2)
    t.pendown()
    t.circle(R2)
    
    t.penup()
    t.goto(R2, 0)
    t.pendown()
    t.fillcolor("gray")
    t.begin_fill()
    t.forward(tsh)
    t.left(90)
    t.circle(R1, 90) 
    t.left(90)
    t.forward(tsh)
    t.left(90)
    t.circle(-R2, 90)
    t.end_fill()

    t.right(90)
    t.forward(R2*2)
    t.begin_fill()
    t.forward(tsh)
    t.left(90)
    t.circle(R1, 90) 
    t.left(90)
    t.forward(tsh)
    t.left(90)
    t.circle(-R2, 90)
    t.end_fill()
    t.hideturtle()

root = Tk()
root.title("Circle Drawing Program")
root.geometry("300x250")

label_r1 = Label(root, text="Enter R1:")
label_r1.grid(row=0)
entry_r1 = Entry(root)
entry_r1.grid(row=0, column=1)

label_r2 = Label(root, text="Enter R2 (R2 < R1):")
label_r2.grid(row=1)
entry_r2 = Entry(root)
entry_r2.grid(row=1, column=1)

draw_button = Button(root, text="Draw Circles", command=draw_circles)
draw_button.grid(row=2, column=1)

def check_point():
    global result
    x = float(entry_x.get())
    y = float(entry_y.get())
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color("red")
    t.begin_fill()
    t.circle(4)
    t.end_fill()
    t.hideturtle()
    if (x**2 + y**2 <= R1**2 and x >= 0 and y >= 0) or (x**2 + y**2 >= R2**2 and x <= 0 and y <= 0):
        result = ("Point is in the gray area.")
    else:
        result = ("Point is not in the gray area.")
    output_label.config(text=f"Result: {result}")


label_x = Label(root, text="Enter x coordinate:")
label_x.grid(row=3)
entry_x = Entry(root)
entry_x.grid(row=3, column=1)

label_y = Label(root, text="Enter y coordinate:")
label_y.grid(row=4)
entry_y = Entry(root)
entry_y.grid(row=4, column=1)

check_button = Button(root, text="Check Point Location", command=check_point)
check_button.grid(row=5, column=1)

output_label = Label(root, text="")
output_label.grid(row=6)

root.mainloop()
