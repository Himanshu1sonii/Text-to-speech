
from logging import RootLogger, root
from tkinter import *
import tkinter
import os
from tkinter import font
from tkinter.constants import RIDGE
from gtts import gTTS


#if you want new file you can change sample.txt
##    abc = open('sample.txt')

##    text = abc.read()   #text that you want to convert.

 ##   language = 'en'  # en is for english language

##    obj = gTTS(text = text,lang= language,slow = False)

##   obj.save("sample.mp3")

##    os.system('sample.mp3')


coro = Tk()
coro.title("Text to Speech")
coro.geometry('800x500+200+100')
coro.configure(bg ='#046173')

mainlabel =  tkinter.Label(coro,text="Text to Speech",font=("new roman",20,"italic bold"), bg = "#05897A" ,width=50
                         ,fg = "black",bd=5)
mainlabel.place(x=0,y=0)

cntdata = StringVar() 
t = Text(coro, font = ("arial",11,"italic bold")  ,height=20, width=90, bg= "#05897A")
t.place(x = 25,y =70)

Submit = tkinter.Button(coro,text= "Submit", bg = "#CB054A", font = ("arial",15,"italic bold"), relief= RIDGE, activebackground = "#7B0519", 
                 activeforeground = "white", bd = 5, width = 25) 
Submit.place(x= 450, y= 430)

coro.mainloop()


