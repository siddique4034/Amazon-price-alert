import smtplib
import os


MY_EMAIL = "mdsiddiquerain@gmail.com"
TO_EMAIL = "siddiquemd4034@gmail.com"
PASSWORD = os.environ['PASSWORD'] #You have to provide your app password here

class SendMail:
   def __init__ (self, product_price, product_link, product_title):
     self.message = f'Subject: Price Alert🚨\n\nThe price of "{product_title}" has dropped to ₹{product_price}\n\n Link 🔗 of Product: {product_link}'.encode("utf-8")
    
     with smtplib.SMTP("smtp.gmail.com") as connection:
       connection.starttls()
       connection.login(user=MY_EMAIL, password=PASSWORD)
       connection.sendmail(
         from_addr=MY_EMAIL, 
         to_addrs=TO_EMAIL, 
         msg=self.message)


