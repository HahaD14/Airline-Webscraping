import requests
from bs4 import BeautifulSoup
import openpyxl

# specify the url
url = 'https://www.example.com/flights'

# send a request to the website
response = requests.get(url)

# parse the HTML content of the website
soup = BeautifulSoup(response.content, 'html.parser')

# find all elements with the class 'ticket-price'
ticket_prices = soup.find_all(class_='ticket-price')

# create a new Excel workbook
workbook = openpyxl.Workbook()

# create a new sheet
sheet = workbook.active

# add a header row
sheet.append(["Ticket Price"])

# add the ticket prices to the sheet
for price in ticket_prices:
    sheet.append([price.text])

# save the workbook
workbook.save("prices.xlsx")
