from tkinter import *# here we are using tkinter package(it pronounce "Tay-kinter" or "kinter". tkinter is the python's GUI(Graphical user interface)toolkit.
#here we are using tkinter for show time graphicaly !
from tkinter.ttk import *#ttk is used here for adding style in our digital clock!

from time import strftime#using time module to show time and strftime to convert integar into string for show hour,minute and second and am or pm

root = Tk()# here we using root = Tk  it makes root for window where time will be show
root.title("Clock")


def time():
    string = strftime('%I:%M:%S %p')
    label.config(text=string) # it configure string into text
    label.after(1000, time) #here time will change after 1 second (1000==1second) and call time function it self


label = Label(root, font=("ds-digital", 80), background="black", foreground="cyan") #we downlond font  from google and install it and here we are using that font "ds-digital".and 80 is the size of font

label.pack(anchor='center')  #here we set our time window or root to center
time()# calling time function

mainloop()# mainloop is used for repeat code.

