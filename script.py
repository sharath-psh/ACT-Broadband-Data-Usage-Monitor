from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import datetime
from requests import get
import csv
import calendar
import datetime
from openpyxl import Workbook



#function to wait 2 seconds
def waiter():
	print("Waiting started")
	time.sleep(2)
	print("Waiting done")

#setting up the driver
print("Setting up the driver")
driver = webdriver.Chrome(executable_path=r"chromedriver.exe")
driver.get("https://selfcare.actcorp.in/group/blr/myaccount")
res = driver.execute_script("return document.documentElement.outerHTML")
print("Driver ready")

#waiting for page load
waiter()

#clicking action
print("Clicking...")
elem=driver.find_element_by_xpath("//span[contains(.,'My Package')]")
elem.click()
print("Done")

waiter()

#extract data using bs4

print("Started Soup")
soup = BeautifulSoup(res, 'lxml')
waiter()
#data usage xpath : //div/div/div/table/tbody/tr[4]
data_usage = driver.find_element_by_xpath("//tr[4]/td[3]")
print("Retrived Data Usage")
#flexbytes xpath: //td/div/div/form
flexbytes_usage = driver.find_element_by_xpath("//table[3]/tbody/tr/td[3]")
print("Retrived flex bytes usage")
data_usage = str(data_usage.text)
flexbytes_usage = str(flexbytes_usage.text)


#close driver
print("Text Extraction complete \nClosing driver")
driver.close()

print("Working on date,time,data calculation...")

#get date,time and IP adress from ipapi
now = datetime.datetime.today().strftime('%Y-%m-%d')
ip = get('https://ipapi.co/ip/').text


#string manipulation to get the proper values
quota = data_usage.split("a")[1]
quota = quota.replace(")","")
quota = quota.replace(" ","")
quota = quota.replace("GB","")
print("Data Usage::\nQuota :",quota)

data_used = data_usage.split("(")[0]
data_used = data_used.replace(" ","")
data_used = data_used.replace("GB","")
print("Data used:", data_used)

flexbytes_quota = flexbytes_usage.split("a")[1]
flexbytes_quota = flexbytes_quota.replace(")","")
flexbytes_quota = flexbytes_quota.replace(" ","")
flexbytes_quota = flexbytes_quota.replace("GB","")
print("Flexbytes Usage::\nflexbytes quota : ",flexbytes_quota)


flexbytes_used = flexbytes_usage.split("(")[0]
flexbytes_used = flexbytes_used.replace(" ","")
flexbytes_used = flexbytes_used.replace("GB","")
print("flexbyetes used : ", flexbytes_used)


#get date
now = datetime.datetime.now()
month_days = calendar.monthrange(now.year, now.month)[1]
month_days = int(month_days)
print("Days in this months : ",month_days)

today_date = datetime.datetime.now()
today_date = today_date.strftime("%d")
today_date = int(today_date)
print("Today's date : ",today_date)

#days left
days_left = month_days-today_date
print("Days left : ",days_left)

#data left
quota =  int(float(quota))
data_used =  int(float(data_used))
data_left = quota-data_used
print("Data left : ",data_left)


#per day how much
per_day = data_left/days_left
per_day =  int(float(per_day))
print("Per day you can use : ",per_day)

#used percentage
usage_percent = (data_used/quota)*100
print("Data Usage percentage",usage_percent)

#total data with flexbytes
flexbytes_quota =  int(float(flexbytes_quota))
total_data=quota+flexbytes_quota
print("Total data : ",total_data)

flexbytes_used =  int(float(flexbytes_used))
total_data_used=data_used+flexbytes_used
print("Total data used : ",total_data_used)

total_data_left=total_data-total_data_used
print("Total data left : ",total_data_left)


#prints the date usage, flexbytes usage,date, time and IP adress
print("Data Usage : ",data_usage)
print("FlexBytes Data Usage:",flexbytes_usage)
print("Date : ",now)
print("IP Adress: ",ip)



#csv writing
myData = [[now,ip,quota,data_used,data_left,flexbytes_quota,flexbytes_used,month_days,today_date,days_left,per_day,usage_percent,total_data,total_data_used,total_data_left]]
myFile = open('output.csv', 'a', newline='')
with myFile:
    writer = csv.writer(myFile)
    writer.writerows(myData)
     

print("CSV Writing complete")

#txt writing
txtfile = open("output.txt","a+") 
with txtfile:
	txtfile.write("\n|\t{0}\t|\t{1}\t|\t{2}\t\t|\t{3}\t|\t{4}\t\t\t\t|\t{5}\t\t\t\t|".format(now,ip,quota,data_used,flexbytes_quota,flexbytes_used))

print("txt Writing complete")

#csv to xlsx
wb = Workbook()
ws = wb.active
with open('output.csv', 'r') as f:
    for row in csv.reader(f):
        ws.append(row)
wb.save('output.xlsx')
print("CSV to xlsx complete")

#all done
print("*****All Done*****")