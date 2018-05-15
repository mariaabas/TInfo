#from icalendar import Calendar, Event
#from datetime import datetime
#from pytz import UTC
#from ics import Calendar, Event 
#import requests
#import urllib2
#from ics import Calendar
#from icalendar import Calendar
#from urllib2 import urlopen # import requests
import requests
import bs4
from icalendar import Calendar, Event

def main():
	#url = "https://raco.fib.upc.edu/api/aules/horari-avui.ics"
  	#req = requests.get(url)
  	#cal = Calendar.from_ical(req.open)
  	#event = cal.walk("VEVENT")
    #for event in cal.walk("VEVENT"):
    #	print(event)
	page = requests.get('https://meded.hms.harvard.edu/calendar').content
	soup = bs4.BeautifulSoup(page, 'lxml')
	link = soup.find('a', attrs={'class': 'subscribe'})
	print(link)
#>>> link
#<a class="subscribe" href="https://meded.hms.harvard.edu/calendar/upcoming/all/export.ics">subscribe</a>
#>>> link.attrs['href']
#'https://meded.hms.harvard.edu/calendar/upcoming/all/export.ics'
#>>> ics = requests.get(link.attrs['href']).content
#>>> open('med_school.ics', 'wb').write(ics)
#1699

	##### import request use #####
  	#req = requests.request('GET', 'https://raco.fib.upc.edu/api/horaris/horari-assignatures.txt?assignatures=GRAU-IC&assignatures=GRAU-PRO1')
	#req = requests.request('GET', 'https://raco.fib.upc.edu//api/aules/horari-avui.ics')
	#gcal = Calendar.from_ical(req.method)
	#print(req)
   #req = requests.request('GET', 'https://raco.fib.upc.edu/api/horaris/horari-assignatures.txt?assignatures=GRAU-IC&assignatures=GRAU-PRO1')
   #print(req.content)
    #################
   #req = urllib2.Request('https://raco.fib.upc.edu/api/aules/horari-avui.ics')
   #response = urllib2.urlopen(req)
   # data = response.read()
   # file = open("testfile.txt","w") 
   # file.write(data)
   # file.close()
   # print(data)
   #req = requests.request('GET', 'https://raco.fib.upc.edu//api/aules/horari-avui.ics')
   #req = urllib2.Request('https://raco.fib.upc.edu//api/aules/horari-avui.ics')
   #response = urllib2.urlopen(req)
   #data = response.read()

   #cal = Calendar.from_ical(data)

   #for event in cal.walk('vevent'):

    #    date = event.get('dtstart')
     #   summery = event.get('summary')

      #  print str(date)
       # print str(summery)

 
  #  cal = Calendar.from_ical(data)

   # print(cal)
   ####################################
   
   #c = Calendar(urlopen(url).read().text())
  #c = Calendar(requests.get(url).text)
   
  # c = Calendar(urlopen(url).read())
  # for component in c.walk():
  #  if component.name == "VEVENT":
  #      print(component.get('LOCATION'))
  #      print(component.get('DTSTART'))
  #      print(component.get('DTEND'))
  #      print(component.get('SUMMARY'))

   
main()
