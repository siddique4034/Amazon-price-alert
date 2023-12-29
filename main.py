import requests
from bs4 import BeautifulSoup
import lxml
from mail import SendMail

URL = "https://www.amazon.in/Rich-Dad-Poor-Middle-Anniversary/dp/1612681131/"

header = {
  "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
  "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

response = requests.get(URL, headers=header)


soup = BeautifulSoup(response.content, "lxml")

title = soup.find(id="productTitle").get_text().strip()
price_element = soup.find(class_="a-offscreen")
price = float(price_element.get_text().split("₹")[1])
alert_price = 420.0


if price <= alert_price:
   message = SendMail(product_price=price, product_link=URL, product_title=title)
   print("Message sent successfully")
  
