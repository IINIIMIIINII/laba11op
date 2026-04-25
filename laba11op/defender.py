from tkinter import *
import math

def triangle():
    canvas.coords(c,(0, 0, 0, 0))
    canvas.coords(r_rect, (0, 0, 0, 0))
    canvas.itemconfig(t, fill='yellow', outline='white')
    canvas.coords (t, (50, 200, 340, 200, 110, 60))
    text.delete(1.0, END)
    text.insert(1.0, "Зображення трикутника")
    text.tag_add('title', '1.0', '1.end')
    text.tag_config('title', font=('Times', 14), foreground='blue')

def triangleXYZ():
    global q, w, e, r_val
    canvas.coords(c,(0, 0, 0, 0))
    canvas.coords(r_rect, (0, 0, 0, 0))
    canvas.itemconfig(t, fill='green', outline='white')
    try:
        x=int(entry_x.get())
        y=int(entry_y.get())
        z=int(entry_z.get())
        if x <= 0 or y <= 0 or z <= 0:
            raise ValueError
        if x + y <= z or x + z <= y or y + z <= x:
            text.delete(1.0, END)
            text.insert(1.0, "Такий трикутник не існує")
            canvas.coords (t, (0, 0, 0, 0, 0, 0))
            return
        Ax, Ay = 50, 250
        scale = 10
        Bx, By = Ax + x * scale, Ay
        cos_angle = (x**2 + y**2 - z**2) / (2 * x * y)
        cos_angle = max(-1, min(1, cos_angle))
        angle = math.acos(cos_angle)
        Cx = Ax + y * scale * math.cos(angle)
        Cy = Ay - y * scale * math.sin(angle)
        canvas.coords(t, (Ax, Ay, Bx, By, Cx, Cy))
        text.delete(1.0, END)
        text.insert(1.0, "Ваш трикутник")
        p = (x + y + z) / 2
        S = math.sqrt(p * (p - x) * (p - y) * (p - z))
        P = x + y + z
        text.insert(END, f"\nПлоща: {S:.2f} \nПериметр: {P:.2f}")

        R = (S / p) * scale 
        a, b, c1 = z, y, x
        Ix = (a*Ax + b*Bx + c1*Cx) / (a + b + c1)
        Iy = (a*Ay + b*By + c1*Cy) / (a + b + c1)
        q,w,e,r_val = Ix - R, Iy - R, Ix + R, Iy + R
        canvas.coords(c, (q, w, e, r_val))
        canvas.itemconfig(c, fill='', outline='black', width=2)

    except ValueError:
        text.delete(1.0, END)
        text.insert(1.0, "Треба вводити додатні числа.")
        canvas.coords (t, (0, 0, 0, 0, 0, 0))

def rectangle():
    canvas.coords (t, (0, 0, 0, 0, 0, 0))
    canvas.coords(c,(0, 0, 0, 0))
    canvas.itemconfig(r_rect, fill='blue', outline='white') 
    canvas.coords(r_rect, (80, 50, 320, 200))
    text.delete(1.0, END) 
    text.insert(1.0, "Зображення прямокутника")
    text.tag_add('title', '1.0', '1.end')
    text.tag_config('title', font=('Times', 14), foreground='black')

def circle():
    canvas.coords (t, (0, 0, 0, 0, 0, 0))
    canvas.coords(r_rect, (0, 0, 0, 0))
    canvas.itemconfig(c, fill='red', outline='white')
    canvas.coords(c, (q, w, e, r_val))
    text.delete(1.0, END) 
    text.insert(1.0, "Зображення кола")
    text.tag_add('title', '1.0', '1.end')
    text.tag_config('title', font=('Times', 14), foreground='red')

def clear():
    canvas.coords (t, (0, 0, 0, 0, 0, 0))
    canvas.coords(r_rect, (0, 0, 0, 0))
    canvas.coords(c,(0, 0, 0, 0))
    text.delete(1.0, END) 

win = Tk()

q, w, e, r_val = 150, 100, 250, 200

b_triangle = Button(text="Трикутник", width=15, command=triangle)
b_rectangle = Button(text="Прямокутник", width=15, command=rectangle)
b_circle = Button(text="Коло", width=15, command=circle)
b_clear = Button(text="Очистити", width=15, command=clear)
b_get = Button(text="Трикутник XYZ", width=15, command=triangleXYZ)

entry_x = Entry(width=15)
entry_y = Entry(width=15)
entry_z = Entry(width=15)

label_x = Label(text='X', font=('Times', 14))
label_y = Label(text='Y', font=('Times', 14))
label_z = Label(text='Z', font=('Times', 14))

canvas = Canvas (width=400, height=300, bg='#fff')
text = Text(width= 55, height=5, bg='#fff', wrap=WORD)

t = canvas.create_polygon(0, 0, 0, 0, 0, 0)
r_rect = canvas.create_rectangle(0, 0, 0, 0)
c = canvas.create_oval(0, 0, 0, 0)

b_triangle.grid(row=0, column=0)
b_rectangle.grid(row=1, column=0)
b_circle.grid(row=2, column=0)
b_clear.grid(row=3, column=0)
entry_x.grid(row=4, column=0)
label_x.grid(row=4, column=1)
entry_y.grid(row=5, column=0)
label_y.grid(row=5, column=1)
entry_z.grid(row=6, column=0)
label_z.grid(row=6, column=1)
b_get.grid(row=7, column=0)

canvas.grid(row=0, column=2, rowspan=10)
text.grid(row=11, column=2, rowspan=3)

win.mainloop()
