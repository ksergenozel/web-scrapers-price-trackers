import requests
from bs4 import BeautifulSoup
import smtplib
from time import sleep
from email.mime.text import MIMEText

URL = "https://www.gittigidiyor.com/ev-elektronigi/briz-br760-zaman-ve-aroma-ayarli-dijital-filtre-kahve-makinesi_pdp_741817415"

desired_price = float(1600)

email = <SENDER_MAIL>
password = <SENDER_MAIL_PASSWORD>

recipient = <RECIPIENT_MAIL>

headers = {
  "User-Agent" : <YOUR USER AGENT>
}

def price_check():
  page = requests.get(URL, headers = headers)
  soup = BeautifulSoup(page.content, "html.parser")
  raw_price_data = soup.find(id="sp-price-lowPrice").getText().strip()
  price = float(raw_price_data[0:-3].split(",")[0].replace(".","")) 
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
  
  subject = "Price Down (Gittigidiyor)"
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
    
  
  







