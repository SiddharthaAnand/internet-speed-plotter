from selenium import webdriver
import time
import csv
import urllib
import sys

def is_connected():
	try :
		url = "https://www.google.com"
		urllib.urlopen(url)
		return True
	except :
		status = "Not connect"
	print status
	return False

def write_csv(speed):
	with open('speed.csv', "a+") as csv_file:
		writer = csv.writer(csv_file)
		writer.writerow(speed)

def speed_test():
	driver = webdriver.Firefox()
	driver.get("https://www.fast.com")
	# minutes in a day
	minutes = 24 * 60
	while minutes != 0:
		time.sleep(60)
		is_online = is_connected()
		if not is_online:
			sys.exit()
		minutes -= 1
		try:
			elem_value = driver.find_element_by_id("speed-value")
			speed_value = elem_value.text.encode('utf-8')
			elem_unit = driver.find_element_by_id("speed-units")
			speed_unit = elem_unit.text.encode('utf-8')
			elem_refresh = driver.find_element_by_id("speed-progress-indicator")
			elem_refresh.click()
			print "Speed now....", speed_value, speed_unit
			# Write the value in csv
			write_csv([speed_value, speed_unit, time.asctime()])
		except Exception as e:
			print "Exception encountered: ", e
			time.sleep(5)
			continue

speed_test()