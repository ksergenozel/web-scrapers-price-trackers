import requests
from bs4 import BeautifulSoup
import smtplib
from time import sleep
from email.mime.text import MIMEText

URL = "https://www.hepsiburada.com/harman-kardon-aura-studio-3-bluetooth-hoparlor-p-HBV00000VFYFU"

desired_price = float(3300)

email = <SENDER_MAIL>
password = <SENDER_MAIL_PASSWORD>

recipient = <RECIPIENT_MAIL>

headers = {
  "User-Agent" : <YOUR USER AGENT>
}

def price_check():
  page = requests.get(URL, headers = headers)
  soup = BeautifulSoup(page.content, "html.parser")
  price = float(soup.find("span", {'data-bind':"markupText:'currentPriceBeforePoint'"}).getText().strip().replace(".",""))
  if (price <= desired_price):
    send_email(price)
    print("Email has been sent.")
  else:
    print("Waiting for discount...")

def send_email(price):
  server = smtplib.SMTP("smtp.gmail.com", 587)
  server.ehlo()
  server.starttls()
  server.ehlo()
  server.login(email, password)
  
  subject = "Price Down (Hepsiburada)"
  content = f"URL: {URL}\n\nCurrent Price: ₺{price}"
  text_subtype = "plain"
  
  msg = MIMEText(content, text_subtype)
  msg['Subject'] = subject
  msg['From'] = email
  
  server.sendmail(email, recipient, msg.as_string())
  
  server.quit()
  
while True:
  price_check()
  sleep(60 * 60)
    
  
  







