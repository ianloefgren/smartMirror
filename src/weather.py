#!/usr/bin/python

from Tkinter import *
import json
import requests

API_KEY = 'eceb3d5a2dbcd2d055f746529a732ca6'
# latitude and longitude for residence 
LATITUDE = 40.000092
LONGITUDE = -105.265552

weather_icons = {}

class Weather(Frame):
	def __init__(self,parent,*args,**kwargs):
		Frame.__init__(self,parent,bg='black')
		self.temperature = ''
		self.hi = ''
		self.low = ''
		self.icon = ''
		self.degreeFrame = Frame(self, bg="black")
        	self.degreeFrame.pack(side=TOP, anchor=W)
        	self.temperatureLabel = Label(self.degreeFrame, font=('Helvetica', 20), fg="white", bg="black")
        	self.temperatureLabel.pack(side=LEFT, anchor=N)
        	self.iconLabel = Label(self.degreeFrame, bg="black")
        	self.iconLabel.pack(side=LEFT, anchor=N, padx=20)
        	self.currentlyLabel = Label(self, font=('Helvetica', 18), fg="white", bg="black")
        	self.currentlyLabel.pack(side=TOP, anchor=W)
        	self.locationLabel = Label(self, font=('Helvetica', 14), fg="white", bg="black")
        	self.locationLabel.pack(side=TOP, anchor=W)
        	self.get_weather()

	def get_weather(self):
		try:
			request_url = "https://api.darksky.net/forecast/%s/%s,%s?" % (API_KEY,LATITUDE,LONGITUDE)
			req = requests.get(request_url)
			weather_obj = json.loads(req.text)
		
			degree_sign = u'\N{DEGREE SIGN}'
			temperature2 = "%s%s" % (str(int(weather_obj['currently']['temperature'])),degree_sign)

			#add icon stuff

			if self.temperature != temperature2:
				self.temperature = temperature2
				self.temperatureLabel.config(text=temperature2)

			#if self.

		except Exception as e:
			print "Cannot retreive weather information. Error: %s" % e

		self.after(600000,self.get_weather)
