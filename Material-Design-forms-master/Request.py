from bs4 import BeautifulSoup
import requests
url=requests.get("http://srtmun.ac.in/en/examination/results.html")

soap=BeautifulSoup(url.text,'html.parser')
#print(soap.prettify())

r=0
link1="http://www.srtmun.ac.in"
'''
for link in soap.find_all('a'):
	links=link.get('href') #List of links
	print(links);
'''
adminform = soap.find_all("table",{"class":'category table table-striped table-bordered table-hover'});#,class='category')	
results = adminform[0].find_all('a')
for i in results:
	print(i.get('href'));
'''	l=str(links) 
	l1=l.split("/")
	print(l1)
	print("")
	for k in l1:
		k1=k
		k1=k1.split("-")
		for k2 in k1:
				if(k2=="civil"):
					r=1
					link1+=link.get('href')'''