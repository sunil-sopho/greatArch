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
# import pyautogui

modes = {"gui":1,"web":2}
# webmode == "headless"
webmode = [""]
driver  = None
debug = 1


def autologin():



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

	text = "This is automation system"

	parser = argparse.ArgumentParser(description = text)

	ip = "www.google.com"
	steps = [[2,"get",ip],[1,"open","sublime"]]

	automate(steps)
