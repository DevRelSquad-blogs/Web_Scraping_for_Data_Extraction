# Python Web Scraping Project: Quotes from Quotes to Scrape

This project demonstrates how to use Python to scrape data from the website [Quotes to Scrape](http://quotes.toscrape.com/). The code fetches quotes, authors, and tags from the site using the `requests` and `BeautifulSoup` libraries, organizes the data, and saves it to a CSV file.

## Table of Contents
- [Features](#features)
- [Technologies](#technologies)
- [Setup](#setup)
- [Usage](#usage)
- [License](#license)

## Features

- Extracts quotes, authors, and tags from each quote on the page.
- Saves the scraped data into a CSV file named `quotes_data.csv`.
- Uses `pandas` to organize and save data efficiently.

## Technologies

- **Python 3.x**
- **requests**: to make HTTP requests.
- **BeautifulSoup**: to parse HTML.
- **pandas**: to manage and save data.

## Setup

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/python-web-scraping-quotes.git
   cd python-web-scraping-quotes
2. Install required packages:
   ```bash
   pip install requests beautifulsoup4 pandas
## Usage

1. Run the script
   ```bash
   python script.py
2. If successful, the script will print Page retrieved successfully and display the data in the terminal. It will also save the data to a CSV file named `quotes_data.csv`.
