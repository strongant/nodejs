# _*_coding: UTF-8_*_
__author__ = 'bwh'

from Tkinter import *
root = Tk()


li = ["C","Python","PHP","html","JAVA"]
movie = ["CSS","jQuery","Bootstrap"]

listb = Listbox(root)
listb2 = Listbox(root)

for item in li:
    listb.insert(0,item)

for item in movie:
    listb2.insert(0,item)

listb.pack()
listb2.pack()
root.mainloop()


