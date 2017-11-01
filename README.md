# speed-test-plotter
The code checks your internet connection speed from [www.fast.com](https://www.fast.com) and 
writes in a csv file.

# How to clone the repository
```
>>> git clone https://github.com/SiddharthaAnand/internet-speed-plotter.git
```

# Dependencies
* selenium

# data
The data stored in the speed.csv file consists of three columns.
```
>>> head speed.csv
25, Mbps, Wed Nov  1 13:29:16 2017
...
```
The vaules denote the speed, unit and time of the day respectively.

# Improvements
* Show real-time values as a plot