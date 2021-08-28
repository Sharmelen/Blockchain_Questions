import wx
import socket
import sys
import hashlib
import os
#from quest_3 import *


def third_question():

	app = wx.App()
	win = wx.Frame(None, title="When Should You Use Blockchain", size=(410, 150))
	win.SetBackgroundColour('white')

	vbox = wx.BoxSizer(wx.VERTICAL)
	font = wx.SystemSettings.GetFont(wx.SYS_SYSTEM_FONT)
	font.SetPointSize(9)
	##############################################################################################################
		
	def account_info(event):
		
		print("hello")
		
	def no_func(event):
		print("no pressed")

	##############################################################################################################
	hbox1 = wx.BoxSizer(wx.HORIZONTAL)
	st1 = wx.StaticText(win, label = "Are you able to create an authoritative and \n permanent record of digital assests ?")

	st1.SetFont(font)
	hbox1.Add(st1)

	vbox.Add(hbox1, flag = wx.CENTER)

	##############################################################################################################

	vbox.Add((-1,20))

	hbox1 = wx.BoxSizer(wx.HORIZONTAL)

	acc_info = wx.Button(win, label = 'Yes', size = (150,30))
	hbox1.Add(acc_info)
	acc_info.Bind(wx.EVT_BUTTON, account_info)

	no_button = wx.Button(win, label = 'No', size = (150,30))
	hbox1.Add(no_button,flag = wx.LEFT, border = 10)
	no_button.Bind(wx.EVT_BUTTON, no_func)


	vbox.Add(hbox1, flag = wx.CENTER)

	win.SetSizer(vbox)

	win.Show()
	app.MainLoop()	
	
third_question()