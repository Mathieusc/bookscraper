from bs4 import BeautifulSoup
import aiohttp
import asyncio
import csv


class BookScraper:
    def __init__(self, book_url):
        self.book_url = book_url
        self.book_data = {}

    async def fetch_book_data(self):
        async with aiohttp.ClientSession() as session:
            async with session.get(self.book_url) as response:
                html = await response.text()
                soup = BeautifulSoup(html, "html.parser")
                # Find the title for example for one book
                print(soup.find("h1").text)
                
                print(soup)

                test = self.extract_product_description(soup)
                print(test)

        return soup

    def extract_product_page_url(self, soup):
        """ADD THIS AT THE END"""
        product_url = ""
        return product_url
    
    def extract_universal_product_code(self, soup):
        upc = soup.find("th", string="UPC").find_next_sibling()
        return upc.text
    
    def extract_title(self, soup):
        title = soup.find("h1")
        return title.text
    
    def extract_price_including_tax(self, soup):
        price_with_tax = soup.find("th", string="Price (incl. tax)").find_next_sibling()
        return price_with_tax.text
    
    def extract_price_excluding_tax(self, soup):
        price_without_tax = soup.find("th", string="Price (excl. tax)").find_next_sibling()
        return price_without_tax.text
    
    def extract_number_available(self, soup):
        number_available = soup.find("p", {"class": "instock availability"})
        return number_available.text.strip()
    
    def extract_product_description(self, soup):
        description = soup.find("h2").find_next()
        return description.text
    
    def extract_category(self, soup):
        category = ""
        return category
    
    def extract_review_rating(self, soup):
        rating = ""
        return rating
    
    def extract_image_url(self, soup):
        image_url = ""
        return image_url
    

    

