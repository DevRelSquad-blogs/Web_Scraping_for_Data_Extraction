import requests
from bs4 import BeautifulSoup
import pandas as pd

# Define the URL
url = 'http://quotes.toscrape.com/'

response = requests.get(url)
if response.status_code == 200:
    print("Page retrieved successfully")
else:
    print("Error retrieving the page")

soup = BeautifulSoup(response.text, 'html.parser')
# Empty lists to store the scraped data
quotes = []
authors = []
tags = []

quote_containers = soup.find_all('div', class_='quote')

# Loop through each container to extract data
for container in quote_containers:
    quote_text = container.find('span', class_='text').text
	quotes.append(quote_text)

    author = container.find('small', class_='author').text
    authors.append(author)
    tag_elements = container.find_all('a', class_='tag')
    tag_text = ', '.join(tag.text for tag in tag_elements)
    tags.append(tag_text)

quotes_df = pd.DataFrame({
    'Quote': quotes,
    'Author': authors,
    'Tags': tags
})

print(quotes_df)
quotes_df.to_csv('quotes_data.csv', index=False)
print("Data saved to quotes_data.csv")
