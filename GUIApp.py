from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image


app = Tk()
app.title("OBD Cluster")
app.geometry('800x480')

master = Canvas(app, width=800, height=480)
master.grid(row=0, column=0)

index = [None]*6
background_img = PhotoImage(file="blueback.gif")
dial_img = PhotoImage(file="dial2.gif")

master.create_image(0, 0, image=background_img, anchor=NW)

radar1 = master.create_image(35, 60, image=dial_img, anchor=NW)
radar2 = master.create_image(310, 60, image=dial_img, anchor=NW)
radar3 = master.create_image(560, 60, image=dial_img, anchor=NW)

radar4 = master.create_image(35, 300, image=dial_img, anchor=NW)
radar5 = master.create_image(310, 300, image=dial_img, anchor=NW)
radar6 = master.create_image(560, 300, image=dial_img, anchor=NW)

