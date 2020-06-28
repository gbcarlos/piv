# -*- coding: utf-8 -*-

from tkinter import *

root = Tk() #creates the window

#Creates the title of the window
wintitle = Label(root, text='Particle Image Velocimetry').pack()

class App:
  def __init__(self, master):
    frame = Frame(master)
    frame.pack()
    self.button = Button(frame, 
                         text="QUIT", fg="red",
                         command=frame.quit)
    self.button.pack(side=LEFT)
    self.slogan = Button(frame,
                         text="Hello",
                         command=self.write_slogan)
    self.slogan.pack(side=LEFT)
  def write_slogan(self):
    print ("Tkinter is easy to use!")

#app = App(root)

#Creates sliders to scale the search and interrogation windows
search_scale = Scale(root, from_=10, to=50, label='Search Window Size',
                     orient=HORIZONTAL, resolution=10).pack()
interr_scale = Scale(root, from_=10, to=50, label='Interrogation Window Size',
                     orient=HORIZONTAL, resolution=10).pack()

mainloop()