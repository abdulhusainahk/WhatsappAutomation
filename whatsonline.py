import time
from datetime import datetime

from playsound import playsound
from selenium import webdriver
from selenium.common.exceptions import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
browser=webdriver.Firefox(executable_path=r"C:\fire\geckodriver.exe")
browser.get("https://web.whatsapp.com/")
wait = WebDriverWait(browser, 60)
target = input("Enter the name of user or group: ")
'''msg=input("Enter your message : ")
count=int(input("Enter the count: "))
user=browser.find_element_by_xpath('//span[@title = "{}"]'.format(name))
user.click()'''
x_arg = '//span[contains(@title, '+ '"' +target + '"'+ ')]'
y_arg = '//span[contains(@title, ' + "online" + ')]'
ONLINE_STATUS_LABEL = '//span[@class=\'O90ur _3FXB1\']'
person_title = wait.until(EC.presence_of_element_located((By.XPATH, x_arg)))
print(target)
person_title.click()
while True:
	i=0
	try:
		status = browser.find_element_by_xpath(ONLINE_STATUS_LABEL).text
		if status != 'online' and status != 'typing...':
			raise NoSuchElementException
		i=1
	except (NoSuchElementException, StaleElementReferenceException):
		status = 'offline'
		i=0
	stat=['offline','online','typing...']
	if status in stat:
		if i == 1:
			playsound('plucky.mp3')
		if status == stat[2]:
			playsound('plucky.mp3')
		print(datetime.now())
		print(status)
		f=open('status.txt','a')
		f.write(target+' ')
		f.write(str(datetime.now())+' ')
		f.write(status+"\n")
		f.close()
	while True:
		if i == 1:
			try:
				status = browser.find_element_by_xpath(ONLINE_STATUS_LABEL).text
				if status=='online':
					continue
				else:
					raise NoSuchElementException
				
			except (NoSuchElementException, StaleElementReferenceException):
				status = 'offline'
				break
		else:
			try:
				status = browser.find_element_by_xpath(ONLINE_STATUS_LABEL).text
				if status=='online':
					break
			except (NoSuchElementException, StaleElementReferenceException):
				status = 'offline'
				continue
	time.sleep(1)