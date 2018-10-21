from fastcli import fastcli
import csv
import datetime as dt
import time
import requests

def connected():
	try:
		r = requests.get('https://fast.com')
		if r.status_code == 200:
			return True
	except:
		return False

def write_csv(speed):
	with open('speed.csv', "a+") as csv_file:
		writer = csv.writer(csv_file)
		writer.writerow(speed)

def speed_test():
	data = fastcli.main()
	print('{:.2f}'.format(data), ' mbps')
	write_csv([dt.datetime.now(),data])

while True:

	if  connected():
		speed_test()
	else:
		print('you cannot connect to fast.com retrying in 5 seconds')
		time.sleep(5)
