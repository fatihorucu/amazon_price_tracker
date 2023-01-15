import requests as rq
from bs4 import BeautifulSoup
import smtplib
# import imaplib
# import lxml
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/107.0.0.0 Safari/537.36",
    "Accept-Language": "tr-TR,tr;q=0.6"
}
response = rq.get(url="https://www.amazon.com.tr/Xiaomi-Wireless-Power-Bank-10000/dp/B09TWRHGWV/""ref=sr_1_4?keyw"
                      "ords=wireless+powerbank&qid=1669049411&qu=eyJxc2MiOiI2LjYzIiwicXNhIjoiNS42OCIsInFz"
                      "cCI6""IjMuOTMifQ%3D%3D&sprefix=wireless+power%2Caps%2C130&sr=8-4", headers=headers)
website = response.text
soup = BeautifulSoup(website, "lxml")
price = soup.select_one(".a-price-whole").text
price_int = int(price.strip(","))
print(price_int)
product_title = soup.select_one("#productTitle").text.strip(" ")
currency = soup.select_one(".a-price-symbol").text

your_price_limit = 565

my_email = "MY E-MAIL"
to_address = "TO E-MAIL"
password = "PW"
with smtplib.SMTP(host="smtp.boun.edu.tr") as connection:
    connection.starttls()  # For Security -- Transfer Layer Security(TLS)
    connection.login(my_email, password)
    connection.sendmail(from_addr=my_email, to_addrs=to_address, msg=f"Hey!\n\n{product_title} is now below "
                                                                     f"{your_price_limit} {currency}")
