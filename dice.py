from tkinter import *
import random 

root = Tk()
root.geometry("900x350")
root.title("Roll Dice")

l1 = Label(root,text='',font =("times",200))

def roll():
    count = ['\u2680','\u2681','\u2682','\u2683','\u2684','\u2685']
    l1.config(text=f'{random.choice(count)}{random.choice(count)}')
    l1.pack()

b1 = Button(root,text = "Click to roll",command=roll)
b1.place(x=435,y=0)

root.mainloop()










              

