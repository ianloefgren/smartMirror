#!/usr/bin/python

from Tkinter import *
import time

class Clock(Frame):
	def __init__(self,parent,*args,**kwargs):
		Frame.__init__(self,parent,bg='black')
		# create time label
		self.time1 = ''
		self.timeLabel = Label(self,font=('Helvetica',18),fg='white',bg='black')
		self.timeLabel.pack(side=TOP,anchor=E)
		
		# create day of week label
		self.dow1 = ''
		self.dowLabel = Label(self,font=('Helvetica',12), fg='white',bg='black')
		self.dowLabel.pack(side=TOP,anchor=E)
		
		# create date label
		self.date1 = ''
		self.dateLabel = Label(self,font=('Helvetica',12), fg='white',bg='black')
		self.dateLabel.pack(side=TOP,anchor=E)
		
		self.update()
		

	def update(self):
		time2 = time.strftime('%I:%M %p')
		dow2 = time.strftime('%A')
		date2 = time.strftime("%b %d, %Y")

		if time2 != self.time1:
			self.time1 = time2
			self.timeLabel.config(text=time2)
		if dow2 != self.dow1:
			self.dow1 = dow2
			self.dowLabel.config(text=dow2)
		if date2 != self.date1:
			self.date1 = date2
			self.dateLabel.config(text=date2)

		self.timeLabel.after(200, self.update)

