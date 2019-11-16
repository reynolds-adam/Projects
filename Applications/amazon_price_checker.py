import requests
from bs4 import BeautifulSoup

url = 'https://www.amazon.com/dp/B07G4MNFS1/ref=sspa_dk_detail_0?psc=1&pd_rd_i=B07G4MNFS1&pd_rd_w=0tre1&pf_rd_p=45a72588-80f7-4414-9851-786f6c16d42b&pd_rd_wg=uOzSd&pf_rd_r=28TPM13C7R936AHWYJHN&pd_rd_r=6a717b03-9742-43fa-9980-b0adeee91ffc&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExSDdBQ1pOQUZMTlJTJmVuY3J5cHRlZElkPUExMDA4ODA5M1BLRlRBMk01SldINyZlbmNyeXB0ZWRBZElkPUEwNzM1MDE1MkNFWkJORFZBMUpXNCZ3aWRnZXROYW1lPXNwX2RldGFpbCZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU='

headers = {
    "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'}

page = requests.get(url, headers=headers)

# soup = BeautifulSoup(page.content, 'html.parser')

# title = soup.find(id="productTitle")

soup1 = BeautifulSoup(page.content, "html.parser")

soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

# title = soup2.find(id= "productTitle").get_text()
price = soup2.find(id="priceblock_ourprice").get_text()
# price.stri

print(price.strip())

price.strip