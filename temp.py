from bs4 import BeautifulSoup
import requests
import smtplib,ssl

def email():
	smtp_server = "smtp.gmail.com"
	port = 587  # For starttls
	sender_email = "s15_jamdade_mahesh@mgmcen.ac.in"
	password = input("Type your email password and press enter: ")
	receiver_email = "maheshmn121@gmail.com"
	# Create a secure SSL context
	context = ssl.create_default_context()

	# Try to log in to server and send email
	try:
	    server = smtplib.SMTP(smtp_server,port)
	    server.starttls(context=context) # Secure the connection
	    val = server.login(sender_email, password)
	    print("Yay Login Success :)")
	    message = input("Enter your MessAge:")
	    val = server.sendmail(sender_email, receiver_email, message)
	    print("email Sent")
	    # TODO: Send email here
	except Exception as e:
	    # Print any error messages to stdout
	    print("Exception occured due to:",e)
	finally:
	    server.quit() 
	    print("Closing Application")


url = "http://srtmun.ac.in/en/examination/results.html"
response = requests.get(url)
soup=BeautifulSoup(response.text,'html.parser')
result_list = soup.table.find_all('a')  #returns a list of results
# print(result_list)
target_link=url
for result in result_list:
	link = result.get('href')
	# print(link)
	if "t-e-" in link:
		target_link += link
	elif "te-" in link:
		target_link += link


# crawling to next Web Page
response = requests.get(target_link)
soup=BeautifulSoup(response.text,'html.parser')
itempage = soup.find("div", {"class": "item-page"}).find('a')
url+=itempage.get('href')
print(url)

#Reading the Results text file
print("Reading the Results text file")
response = requests.get(url)
file=BeautifulSoup(response.text,'html.parser')
print(file.prettify())
