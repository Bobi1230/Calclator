from curses import window
from textwrap import fill
import tkinter as tk
from tkinter import *
from turtle import width
window = tk.Tk()


rowFirstNumnber = 1
rowSecondNumnber = 2
rowThirdNumnber = 3


count = 0
def entry_text(number):
    global count
    numbers.insert(count,number)
    count +=1
    #a = int(number)
    #print(a)

#entry text
numbers = tk.Entry()
numbers.grid(row=0,column=0,columnspan=6,sticky=W+E)

w = 1
h =1
#1
butt1= tk.Button(window,text = "1",bg="blue", fg ="red",height=h,width=w,command = lambda: entry_text("1"))
butt1.grid(row =rowFirstNumnber,column=0)
#2
butt2= tk.Button(window,text = "2",bg="blue", fg ="red",height=h,width=w,command = lambda: entry_text("2"))
butt2.grid(row =rowFirstNumnber,column=1)
#3
butt3= tk.Button(window,text = "3",bg="blue", fg ="red",height=h,width=w,command = lambda: entry_text("3"))
butt3.grid(row =rowFirstNumnber,column=2)
#4
butt4= tk.Button(window,text = "4",bg="blue", fg ="red",height=h,width=w,command = lambda: entry_text("4"))
butt4.grid(row =rowSecondNumnber,column=0)
#5
butt5= tk.Button(window,text = "5",bg="blue", fg ="red",height=h,width=w,command = lambda: entry_text("5"))
butt5.grid(row =rowSecondNumnber,column=1)
#6
butt6= tk.Button(window,text = "6",bg="blue", fg ="red",height=h,width=w,command = lambda: entry_text("6"))
butt6.grid(row =rowSecondNumnber,column=2)
#7
butt7= tk.Button(window,text = "7",bg="blue", fg ="red",height=h,width=w,command = lambda: entry_text("7"))
butt7.grid(row =rowThirdNumnber,column=0)
#8
butt8= tk.Button(window,text = "8",bg="blue", fg ="red",height=h,width=w,command = lambda: entry_text("8") )
butt8.grid(row =rowThirdNumnber,column=1)
#9
butt9= tk.Button(window,text = "9",bg="blue", fg ="red",height=h,width=w,command = lambda: entry_text("9"))
butt9.grid(row =rowThirdNumnber,column=2)
#0
butt0= tk.Button(window,text = "0",bg="blue", fg ="red",height=h,width=w,command = lambda: entry_text("0"))
butt0.grid(row =4,column=1)
#+
plus_butt= tk.Button(window,text = "+",bg="blue", fg ="red",height=h,width=w,command = lambda: entry_text(""))
plus_butt.grid(row =1,column=3)
#-
minus_butt= tk.Button(window,text = "-",bg="blue", fg ="red", height=h,width=w,command = lambda: entry_text(""))
minus_butt.grid(row =2,column=3)
#*
mult_butt= tk.Button(window,text = "*",bg="blue", fg ="red",height=h,width=w,command = lambda: entry_text(""))
mult_butt.grid(row =3,column=3)
#/
division_butt= tk.Button(window,text = "/",bg="blue", fg ="red",height=h,width=w,command = lambda: entry_text(""))
division_butt.grid(row =4,column=2)
#clear
clear_butt= tk.Button(window,text = "C",bg="blue", fg ="red",height=h,width=w,command = lambda: entry_text(""))
clear_butt.grid(row =4,column=0)
#equal 
equal = tk.Button(window,text ="=",fg ="red", bg="blue")
equal.grid(row =4,column=3)
#buttons_frame.pack(fill="both",expand = True)
window.geometry("200x200")
window.mainloop()

