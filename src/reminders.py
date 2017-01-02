#!/usr/bin/python

from Tkinter import *
from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

import datetime
import os

SCOPES = 'https://www.googleapis.com/auth/calendar.readonly'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'smartMirror'

class Calendar(Frame):
	def __init__(self,parent,*args,**kwargs):
		Frame.__init__(self,parent,bg='black')
		self.title = 'Calendar Events'
		self.calendarLabel = Label(self,text=self.title,font=('Helvetica',20),fg="white",bg="black")
		self.calendarLabel.pack(side=TOP,anchor=E)
		self.get_events()

	def get_events(self):
		credentials = get_credentials()
		http = credentials.authorize(httplib2.Http())
		service = discovery.build('calendar','v3',http=http)

		now = datetime.datetime.utcnow().isoformat() + 'Z' # Z indicates UTC time
		print('Getting events...')
		events_result = service.events().list(calendarId='primary',timeMin=now,maxResults=10,singleEvents=True,
							orderBy='startTime').excecute()
		events = events_result.get('items',[])

		

	def get_credentials(self):
		home_dir = os.path.expanduser('~')
		credential_dir = os.path.join(home_dir,'.credentials')
		credential_path = os.path.join(credential_dir,'client_secret_user1.json')
		
		store = Storage(credential_path)
		credentials = store.get()


class CalendarEvent(Frame):
	def __init__(self,parent,event_name='Event 1'):
		Frame.__init__(self,parent,bg='black')
		self._event_name = event_name
		self.event_name_label = Label(self,text=self._event_name,font=('Helvetica',14),fg="white",bg="black")
		self.event_name_label.pack(side=TOP,anchor=E) 

			
			
