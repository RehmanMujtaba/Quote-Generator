import requests
from bs4 import BeautifulSoup

def get_quotes(url):
    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'lxml')

    quote_divs = soup.find_all('div', class_="quote")

    quotes = []

    for quote_div in quote_divs:

        quoteText = quote_div.find('div', class_="quoteText")
        
        quote_lines = quoteText.text.strip().split("\n")

        quote, author = quote_lines[0], quote_lines[-1].strip()

        quotes.append({
            'Quote': quote,
            'Author': author
        })

    return quotes

url = 'http://www.goodreads.com/quotes?page=1'
quotes = get_quotes(url)

for quote in quotes:
    print(quote.get('Quote'), ' - ', quote.get('Author'))
