import random
import sys
import os
from tkinter import *
from turtle import back
from PIL import ImageTk, Image

root = Tk()
root.title("Inspire me")
root.resizable(1, 0)
root.geometry('250x200')

# FIX FOR PYINSTALLER NOT SHOWING IMAGE WHEN CONVERTING TO EXE


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


icoImage = PhotoImage(file=resource_path("inspireme.png"))
root.iconphoto(True, icoImage)

delete = False

img1 = Image.open(resource_path("quotesBG.png")).resize((1330, 100))
bgimg = ImageTk.PhotoImage(img1)
#img2 = Image.open("real projects/mini backbutton.png")
#backButton_image = ImageTk.PhotoImage(img2)
reloadImage = PhotoImage(
    file=resource_path("reload.png"))
backButton_image = PhotoImage(file=resource_path("mini backbutton.png"))

quotes = ["You’ve gotta dance like there’s nobody watching, \n love like you’ll never be hurt, \n sing like there’s nobody listening, and live like it’s heaven on earth.” ― William W. Purkey",
          "“Fairy tales are more than true: not because they tell us that dragons exist,\n but because they tell us that dragons can be beaten.”― Neil Gaiman",
          "“Everything you can imagine is real.”― Pablo Picasso",
          "“When one door of happiness closes, another opens; \n but often we look so long at the closed door that we do not see the one which has been opened for us.” ― Helen Keller",
          "“Do one thing every day that scares you.”― Eleanor Roosevelt",
          "“It’s no use going back to yesterday,\n because I was a different person then.”― Lewis Carroll",
          "“Smart people learn from everything and everyone, average people from their experiences, \n stupid people already have all the answers.” – Socrates",
          "“Do what you feel in your heart to be right – for you’ll be criticized anyway.”― Eleanor Roosevelt",
          "“Happiness is not something ready made. \n It comes from your own actions.” ― Dalai Lama XIV",
          "“Whatever you are, be a good one.” ― Abraham Lincoln"]


def suggetions():
    global reload_Button
    global text_label
    global bgLabel
    global backButton
    global reload_Button
    suggest_button.destroy()

    root.minsize(1332, 100)
    root.maxsize(1332, 100)
# backgroud image
    bgLabel = Label(root, image=bgimg)
    bgLabel.grid(row=0, column=0)
# random text
    text_label = Label(root, text=random.choice(quotes),
                       font="Helvetica, 15", fg="Red")
    text_label.grid(row=0, column=0)

    root.geometry('')
    root.resizable(True, False)
#    root.grid_columnconfigure(1, weight=1)
#    root.grid_rowconfigure(0, weight=1)
# backbutton
    backButton = Button(root, image=backButton_image,
                        borderwidth=0, command=backpage)
    backButton.grid(
        row=0, column=0, sticky=NW)
# reload button
    reload_Button = Button(root, image=reloadImage,
                           borderwidth=0, command=reload)
    reload_Button.grid(
        row=0, column=0, sticky=SE)


def reload():
    global delete
    global Reloadtext
    global reload_Button
    if delete == False:
        text_label.destroy()
        delete = True
        Reloadtext = Label(root, text=random.choice(quotes),
                           font="Helvetica, 15", fg="Red")
        Reloadtext.grid(row=0, column=0)
        reload_Button.grid(
            row=0, column=0, sticky=SE)
    if delete == True:
        Reloadtext.destroy()
        Reloadtext = Label(root, text=random.choice(quotes),
                           font="Helvetica, 15", fg="Red")
        Reloadtext.grid(row=0, column=0)
        reload_Button.grid(
            row=0, column=0, sticky=SE)


def backpage():
    global delete
    global Reloadtext
    global suggest_button
    root.minsize(250, 200)
    root.maxsize(250, 200)
    root.geometry('150x100')
    root.resizable(1, 0)
    bgLabel.destroy()
    text_label.destroy()
    backButton.destroy()
    reload_Button.destroy()
    if delete == True:
        Reloadtext.destroy()
    suggest_button = Button(root, text="suggested by me",
                            command=suggetions)
    suggest_button.pack(anchor=CENTER, pady=(60, 0))


suggest_button = Button(root, text="suggested by me",
                        command=suggetions)
suggest_button.pack(anchor=CENTER, pady=(60, 0))


root.mainloop()
