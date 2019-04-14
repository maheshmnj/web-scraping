from bs4 import BeautifulSoup
import requests
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders

msg= MIMEMultipart()
recipents=['onkarbangale44@gmail.com','maheshmn121@gmail.com']
msg['To']=",".join(recipents)
msg['From']="s15_bangale_omkar@mgmcen.ac.in"
password="Mimarathi@1"



url=requests.get("http://srtmun.ac.in/en/examination/results.html")

soap=BeautifulSoup(url.text,'html.parser')
#print(soap.prettify())

r=0
link1="http://www.srtmun.ac.in"
for link in soap.find_all('a'):
	s=link.get('href')
	l=str(s)
	l1=l.split("/")
	for k in l1:
		k1=k
		k1=k1.split("-")
		for k2 in k1:
				if(k2=="civil"):
					r=1
					link1+=link.get('href')

if(r==1):
	link2="http://www.srtmun.ac.in"
	url1=requests.get(link1)
	soap1=BeautifulSoup(url1.text,'html.parser')
	#print(soap1.prettify())
	p=0

	for link3 in soap1.find_all('a'):
		s1=link3.get_text()
		p2=s1.split(" ")
		for k3 in p2:
			if(k3=="T.E."):
				p=1
				link2+=link3.get('href')
	if(p==1):
		url2=requests.get(link2)
		soap2=BeautifulSoup(url2.text,'html.parser')
		f=open("A.txt","a")
		sp=str(soap2)
		f.write(sp)
		fname="A.txt"
		attach=open("A.txt","rb")
		w=MIMEBase('application','octet-stream')
		w.set_payload((attach).read())
		encoders.encode_base64(w)
		w.add_header('content-Disposition',"attach; fimename=%s" %fname)
		msg.attach(w)
		m=smtplib.SMTP('smtp.gmail.com',587)
		m.starttls()
		m.login(msg['from'],password)
		m.sendmail(msg['From'],recipents,msg.as_string())
		m.quit()
		print("hello")


'''<a href="/en/examination/results/9946-t-e-civil-cgpa-new-winter-2018.html">
								T.E. CIVIL (CGPA/NEW) WINTER-2018							</a>'''