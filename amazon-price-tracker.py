import requests
from bs4 import BeautifulSoup
import smtplib
from time import sleep
from email.mime.text import MIMEText

URL = "https://www.amazon.com.tr/Xiaomi-Mi-Band-Ak%C4%B1ll%C4%B1-Bileklik/dp/B091G3FLL7/ref=sr_1_1?__mk_tr_TR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=196R3FHOWBWD5&keywords=xiaomi+mi+band+6&qid=1638748865&sprefix=xiaomi+mi+band%2Caps%2C244&sr=8-1"

desired_price = float(400)

email = <SENDER_MAIL>
password = <SENDER_MAIL_PASSWORD>

recipient = <RECIPIENT_MAIL>

headers = {
  "User-Agent" : <YOUR USER AGENT>
}

def price_check():
  page = requests.get(URL, headers = headers)
  soup = BeautifulSoup(page.content, "html.parser")
  raw_price_data = soup.find(class_="a-offscreen").getText().strip()
  price = float(raw_price_data[0:-2].replace(",",".")) 
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
  
  subject = "Price Down (Amazon)"
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
    
  
  







