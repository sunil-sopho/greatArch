import sys
import argparse
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import staleness_of
from contextlib import contextmanager
# from bs4 import BeautifulSoup
from PIL import Image
from io import BytesIO
from datetime import datetime,timedelta
import os
import ctypes
from ruletester import ruletester
from lexer import lexerGrt
# import pyautogui

modes = {"gui":1,"web":2}
# webmode == "headless"
webmode = [""]
driver  = None
debug = 1
version = "0.0.1" # version of system builds

def autologin():

	return None


def setWeb():
	global driver
	if not driver:
		options = webdriver.ChromeOptions() # define options
		if  "headless" in webmode:
			options.add_argument("headless") # pass headless argument to the options
		if "fullscreen" in webmode:
			options.add_argument("--window-size=1920,1080")
		driver = webdriver.Chrome(executable_path=r"./chromedriver_win32/chromedriver.exe",chrome_options=options)

	return driver
	 

def webAuto(step):
	return
	dr = setWeb()
	if step[1] == "get":
		if debug > 0:
			print("get request at : ",step[2] )
		dr.get("https://www.facebook.com")
	
def exitAll():
	global driver
	if driver:
		driver.quit()

def automate(steps):
	for x in steps:
		if 'int' not in str(type(x[0])):
			x[0] = modes[x[1]]
		if x[0] == 2:
			webAuto(x)
		if x[0] == 1:
			guiAuto(x)

	exitAll()

if __name__ == '__main__':
	"""
	Main fucntion
	Author : Sunil Kumar
	Description : begin the revolution
	"""

	text = "This is automation system : beta project"
	parser = argparse.ArgumentParser(description = text) 
	parser.add_argument("rule",nargs=1, help="<location of rule *.grt>")
	parser.add_argument("-v", "--version", help="show program version",version="program version :: "+version, action="version")
	parser.add_argument("-d", "--debug", help="set debug to True",default=False, action="store_true")
	parser.add_argument("-dm", "--debugMode",choices=['user','dev'],default='user', help="set debugmode by default user")
	parser.add_argument("-o", "--outputMode",choices=['json','csv'],default='csv', help="set outputMode by default csv")
#	parser.add_argument("-p", "--pyversion",choices=['2','3'],default='3', help="set python mode")

	args = parser.parse_args()  
	parser = argparse.ArgumentParser(description = text)


	filename = args.rule[0]
	characters  = "<empty>" 
	try:
		file = open(filename, "r")
		characters = file.read()
		# characters += '\n' # adding endline character at end

		file.close()
	except IOError:
		sys.stderr.write("Error: Rule File does not appear to exist.")
		sys.exit(-1)


	error = ruletester(characters)
	if(error):
		"""
		Exit if rule file is not read
		"""
		sys.stderr.write("Error found in rule")
		sys.exit(-1)

	steps = lexerGrt(characters)
	print(steps)

	# automate(steps)
