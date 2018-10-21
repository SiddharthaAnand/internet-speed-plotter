from fastcli import fastcli
import csv
import datetime as dt
import requests

def connected():
	r = requests.get('https://fast.com')
	if r.status_code == 200:
		return True
	else:
		return False

def write_csv(speed):
	with open('speed.csv', "a+") as csv_file:
		writer = csv.writer(csv_file)
		writer.writerow(speed)

def speed_test():
	data = fastcli.main()
	print('{:.2f}'.format(data), ' mbps')
	write_csv([dt.datetime.now(),data])

while connected():
	speed_test()
