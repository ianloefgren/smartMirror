#!/usr/bin/python

from Tkinter import *
import locale
import threading
import time

from clock import Clock
from weather import Weather

class FullscreenWindow:
	def __init__(self):
		self.tk = Tk()
		self.tk.configure(background='black')
		self.topFrame = Frame(self.tk,background='black')
		self.bottomFrame = Frame(self.tk,background='black')
		self.topFrame.pack(side=TOP,fill=BOTH,expand=YES)
		self.bottomFrame.pack(side=TOP,fill=BOTH,expand=YES)
		self.state = True
		self.tk.bind("<Return>",self.toggle_fullscreen)
		self.tk.bind("<Enter>",self.end_fullscreen)

		# clock
		self.clock = Clock(self.topFrame)
		self.clock.pack(side=RIGHT,anchor=N,padx=100,pady=60)		

		# weather
		self.weather = Weather(self.topFrame)
		self.weather.pack(side=LEFT,anchor=N,padx=100,pady=60)

	def toggle_fullscreen(self, event=None):
		self.state = not self.state #toggle boolean
		self.tk.attributes("-fullscreen",self.state)
		return "break"

	def end_fullscreen(self, event=None):
		self.state = False
		self.tk.attributes("-fullscreen",self.state)
		return "break"

if __name__ == '__main__':
	w = FullscreenWindow()
	w.tk.mainloop()
	
