# coding:utf-8
import tkinter as tk
from tkinter import *

root = tk.Tk()
list = ["西施","王昭君","貂蝉","杨玉环"]
v = []
j = 0
for i in list:
    v.append(IntVar())
    b = Checkbutton(root,text = i,justify = LEFT, variable = v[-1])
    # b.pack(anchor = W,side = LEFT,expand = YES)
    b.grid( row = j,column = 0 )
    a = Label(root, justify = RIGHT,textvariable=v[-1])
    # a.pack(anchor = W,side = RIGHT,expand = YES)
    a.grid(row=j, column=1)
    j += 1

# for i in range(4):
#     a = Label(root,textvariable = v[i])
#     a.pack()
mainloop()
# root = tk.Tk()
# v =IntVar()
# c = Checkbutton(root,text = "测试",variable = v)
# c.pack()
# l = Label(root,textvariable = v)
# l.pack()
# mainloop()

# def callback():
#     var.set("你是个人才！")
# root = tk.Tk()
# frame1 = Frame(root)
# frame2 = Frame(root)
# var = StringVar()
# var.set("hello world!")
# textLabel = Label(frame1,textvariable = var,justify = LEFT)
# textLabel.pack(side = LEFT)
# photo = PhotoImage(file = "bg1.png")
# imgLable1 = Label(frame1,image = photo)
# imgLable1.pack(side = RIGHT)
# theButto = Button(frame2,text = "terday is a nice day!",command = callback)
# theButto.pack()
# frame1.pack(padx = 10,pady = 10)
# frame2.pack(side = RIGHT,padx = 10,pady = 10)
# mainloop()


# root = tk.Tk()
# photo = PhotoImage(file = "bg.png")
# Leabl1 = Label(root,text = "hello world",justify = LEFT,
#                image = photo,compound = CENTER, fg = "black")
# Leabl1.pack()

# mainloop()
# class app(object):
#     def __init__(self,root):
#         frame = tk.Frame(root)
#         frame.pack()
#         self.say = Button(frame,text="dazhaohu",bg = "black",fg = "white",command=self.say_hi)
#         self.say.pack(side=LEFT)
#     def say_hi(self):
#         print("hello world")
#
# root = tk.Tk()
# App = app(root)
#
# root.mainloop()

# root = tk.Tk()
# root.title("my test")
# thelable = tk.Label(root,text = "first form ")
# thelable.pack()
# root.mainloop()
