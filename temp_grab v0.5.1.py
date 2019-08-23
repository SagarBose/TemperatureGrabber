##This script downloads data from https://www.timeanddate.com/
##for the entire year from January to December in TXT Format
##And Saves in a text file in the same folder. Parsed CSV WIP
##This script is valid only for 2016, 2017 and 2018.
##City, Country are to be entered in lower case only.
##Check City and Country spellings from https://www.timeanddate.com/weather/india/bangalore/historic
##And then go to text box for selecting city
## Libraries to install: Beautifulsoup4 , Requests, lxml, csv

from bs4 import BeautifulSoup as bs
import requests
import csv
import re

##Uncomment following section if arguments are to be entered
##while running the program. Enter City, followed by Country
##and then the year. e.g temp_grab.py bangalore india 2018
##print ("Proceeding with data extraction for", sys.argv[1], ",", sys.argv[2], sys.argv[3])
##City=sys.argv[1]
##Country=sys.argv[2]
##Year=sys.argv[3]

Country = input("Enter Country Name(lower case): ")
City = input("Enter City Name(lower case): ")
Year = input("Enter Year for which data is required: ")
if Country.isdigit():
    print("Country Entered is not Valid. Exiting...")
    exit()
if City.isdigit():
    print("City Entered is not Valid. Exiting...")
    exit()
if not(Year.isdigit() and int(Year)>2015 and int(Year)<2019):
    print("Year Entered is not within range or invalid. Exiting...")
    exit()
print("Proceeding with data extraction for", City,",",Country, Year)

i=1
finalString=""
while i<13:                                                                 ##loop to get data for 12 months
    month=str(i)
    URL="https://www.timeanddate.com/weather/"+Country+'/'+City+"/historic?month="+month+"&year="+Year
    #print(URL)
    print("Extracting Temperature Data for month", i, Year)
    soup = bs(requests.get(URL).text,'lxml')                                #convert URL to Beautiful Soup Object
    match = soup.find_all('script', type="text/javascript")[3].text.strip() #fourth data value in the Beautiful Soup Object
    finalString=finalString+','+re.findall('(?<=\[).+?(?=\])',match)[0]     #regex to find everything between the first [] brackets
    i += 1
    

##Removing Characters which dont matter. Also, Formatting the text output.

FormattedString=finalString.replace('},{','\n').replace(',{','').replace('}','').replace(',"temp":','\t').replace('"date":','')
filename=City+" "+Year+".txt"
file=open(filename, "w+")
file.write(FormattedString)
file.close()

##=((((LEFT(A1,10) & "." & RIGHT(A1,3))/60)/60)/24)+DATE(1970,1,1)
