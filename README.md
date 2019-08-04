# ACT-Broadband-Data-Usage-Monitor
Extracts data usage,flexbytes,public ip address of your ACT Broadband and stores it in CSV,txt and xlsx files.

# Introduction

This script will run a selenium webdriver to scrape your data usage from ACT website. Along with this it'll also fetch your public address from ipapi.co. Once this is done, the script will then calculate data quota, used, left, flexbytes quota,used,left, number of days left this month(as data renewal in ACT is every month), amount of data you can use per day for the rest of the month. All of these values are then stored in a CSV, txt and an excel spreadsheet.

# How-to

```
pip install requirements.txt
```

double click on script.py

# Screenshots

CMD : 
![cmd](https://user-images.githubusercontent.com/21749342/54883928-f2f65d80-4e90-11e9-8ea0-7c6010f1b511.PNG)
CSV
![csv](https://user-images.githubusercontent.com/21749342/54883929-f38ef400-4e90-11e9-87a6-ea1ffc9209cf.PNG)
TXT
![txt](https://user-images.githubusercontent.com/21749342/54883930-f38ef400-4e90-11e9-92ec-06e288da2191.PNG)
xlsx
![xl](https://user-images.githubusercontent.com/21749342/54883931-f38ef400-4e90-11e9-84ec-24305f6f2dcd.PNG)

# Todo

* web interface
* browser extention
* fix xlsx type
* fix txt format
