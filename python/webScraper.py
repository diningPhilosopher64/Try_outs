import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText



def connection():
  session = requests.Session()
  credentials = {'username':'MT2018119','password':'Qwertyui1@'}

  webPage = "https://lms.iiitb.ac.in/moodle/login/index.php"
  response  = session.post(webPage, data  = credentials,verify = False)
  html = response.content
  homePage = "https://lms.iiitb.ac.in/moodle/mod/forum/view.php?id=8348"
  response = session.get(homePage,verify= False)
  scraper(response)



def scraper(response):
  soup = BeautifulSoup(response.text,"html.parser")
  tablerow = soup.find('tr',{'class','discussion r0'})
  tabledata = tablerow.find_all('td')
  #subject of post
  topicStarter = tabledata[0].get_text()  
  #Author of post
  Author = tabledata[2].get_text() 
  #link inside post
  link = tabledata[4].find('a').get('href')
  topicStarter = topicStarter + " - " + Author
  #send mail
  sendMail(topicStarter,Author,link)



def sendMail(topicStarter,Author,link):
  TEXT = "Hello all, \n  Announcement : \n " + link
  message = 'Subject: {}\n\n{}'.format(topicStarter, TEXT)

  sender  = "sender@xyz.com"
  to = "reciever@xyz.com"
  gmailUsername = sender
  gmailPassword = "gmailPassowrd"
  s = smtplib.SMTP('smtp.gmail.com', 587)
  s.starttls()
  s.login(gmailUsername, gmailPassword)
  s.sendmail(sender,to,message)
  s.quit()


if __name__ == '__main__':
  connection()