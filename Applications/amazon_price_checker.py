import requests
from bs4 import BeautifulSoup
import smtplib

# url from amazon item
url = 'https://www.amazon.com/dp/B07G4MNFS1/ref=sspa_dk_detail_0?psc=1&pd_rd_i=B07G4MNFS1&pd_rd_w=0tre1&pf_rd_p=45a72588-80f7-4414-9851-786f6c16d42b&pd_rd_wg=uOzSd&pf_rd_r=28TPM13C7R936AHWYJHN&pd_rd_r=6a717b03-9742-43fa-9980-b0adeee91ffc&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExSDdBQ1pOQUZMTlJTJmVuY3J5cHRlZElkPUExMDA4ODA5M1BLRlRBMk01SldINyZlbmNyeXB0ZWRBZElkPUEwNzM1MDE1MkNFWkJORFZBMUpXNCZ3aWRnZXROYW1lPXNwX2RldGFpbCZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU='

# User agent found by searching "my user agent on Google"
headers = {
    "<My User Agent>'}

page = requests.get(url, headers=headers)

# function to check if the price of the item is below a desired threshold and sends an email if so
def check_price():
    soup1 = BeautifulSoup(page.content, "html.parser")
    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    email_title = soup2.find(id= "productTitle").get_text().strip()
    price = soup2.find(id="priceblock_ourprice").get_text().strip()
    converted_price = float(price[1:])

    # price check of desired price 
    if converted_price < 340:
        send_email(title = email_title, price = price)

# function that sends the email
def send_email(title, price):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    # login to email using two-step google verification app password
    server.login('adamreynoldsdata@gmail.com', ,'<password>')

    subject = 'Price Drop to ' + str(price) +' on Sony Headphones'
    body = 'Check the Amazon link: ' + str(url)
    msg = f"Subject: {subject} \n\n {body}"

    server.sendmail(
        from_addr = 'adamreynoldsdata@gmail.com',
        to_addrs = 'adamreynolds89@gmail.com',
        msg = msg
    )
    print('Email has been sent!')


check_price()