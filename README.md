# speed-test-plotter
The code checks your internet connection speed from [www.fast.com](https://www.fast.com) and 
writes in a csv file. The code uses selenium webdriver for firefox and in an interval of 60 seconds 
keeps checking the speed of your internet connection.

## Dependencies
* [selenium](http://selenium-python.readthedocs.io/)
The steps to install and usage are provided in the link.

## How to clone the repository
```
>>> git clone https://github.com/SiddharthaAnand/internet-speed-plotter.git
```

## Running the code
```
>>> python speed_test.py
```

## data
The data stored in the speed.csv file consists of three columns.
```
>>> head speed.csv
25, Mbps, Wed Nov  1 13:29:16 2017
...
```
The vaules denote the speed, unit and time of the day respectively.

## Improvements
* Show real-time values as a plot
* Detect network disconnection and stop
