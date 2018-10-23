from selenium import webdriver
import requests
import time
import csv

url = "https://www.fast.com"


def write_csv(speed):
    with open('speed.csv', "a+") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(speed)


def check_disconnection():
    timeout = 10
    try:
        _ = requests.get(url, timeout=timeout)
        return False
    except requests.RequestException:
        print("Houston, we have a connection problem :( ... retrying in 60 seconds...")
        time.sleep(60)
        return True


def speed_test():
    driver = webdriver.Firefox()
    driver.get(url)
    # minutes in a day
    minutes = 24 * 60
    while minutes != 0:
        if check_disconnection():
            minutes -= 1
            continue
        time.sleep(60)
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
