import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "http://books.toscrape.com/"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

books = soup.find_all("article", class_="product_pod")

data = []

for book in books:
    title = book.h3.a["title"]
    price = book.find("p", class_="price_color").text
    availability = book.find("p", class_="instock availability").text.strip()
    
    rating_class = book.find("p", class_="star-rating")["class"][1]
    
    data.append({
        "Title": title,
        "Price": price,
        "Availability": availability,
        "Rating": rating_class
    })

df = pd.DataFrame(data)
df.to_csv("books.csv", index=False)

print("Scraping complete. Data saved to books.csv")