"""
Developed by Manoj Tyagi
"""

import os
import tkinter.messagebox

from tkinter import *
from tkinter import filedialog

from pygame import mixer

root = Tk()


# Creating the menubar
menubar = Menu(root)
root.config(menu=menubar)

# CReating the submenu
subMenu = Menu(menubar, tearoff=0)


def browse_file():
    global filename
    filename = filedialog.askopenfilename()


menubar.add_cascade(label="File", menu=subMenu)
subMenu.add_command(label="Open", command=browse_file)
subMenu.add_command(label="Exit", command=root.destroy)



def about_us():
    tkinter.messagebox.showinfo('About Sim', 'This is a music player built using Python Tkinter by Manoj Tyagi')


subMenu = Menu(menubar, tearoff=0)

menubar.add_cascade(label="Help", menu=subMenu)
subMenu.add_command(label="About Us", command=about_us)

# Initializing the mixer
mixer.init()

root.geometry('300x300')
root.title('Sim')


text = Label(root, text="Let's make some noise!")
text.pack()


def stop_music():
    mixer.music.stop()
    statusbar['text'] = "Music Stopped"

def play_music():
    mixer.music.play()
    statusbar['text'] = "Music Playing"


def pause_music():
    global paused
    paused = True
    mixer.music.pause()
    statusbar['text'] = "Music Paused"


def set_vol(val):
    volume = int(val)/100
    mixer.music.set_volume(volume)


playPhoto = PhotoImage(file='play.png')
playBtn = Button(root, image=playPhoto, command=play_music)
playBtn.pack()


stopPhoto = PhotoImage(file='stop.png')
stopBtn = Button(root, image=stopPhoto, command=stop_music)
stopBtn.pack()


pausePhoto = PhotoImage(file='pause.png')
pauseBtn = Button(root, image=pausePhoto, command=pause_music)
pauseBtn.pack()


scale = Scale(root, from_=0, to=100, orient=HORIZONTAL, command=set_vol)
scale.set(70)
mixer.music.set_volume(0.7)
scale.pack()

statusbar = Label(root, text="Welcome to Sim", relief=SUNKEN, anchor=W)
statusbar.pack(side=BOTTOM, fill=X)

root.mainloop()