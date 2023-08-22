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

                test = self.extract_title(soup)
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
        price_with_tax = ""
        return price_with_tax
    
    def extract_price_excluding_tax(self, soup):
        price_without_tax = ""
        return price_without_tax
    
    def extract_number_available(self, soup):
        number_available = ""
        return number_available
    
    def extract_product_description(self, soup):
        description = ""
        return description
    
    def extract_category(self, soup):
        category = ""
        return category
    
    def extract_review_rating(self, soup):
        rating = ""
        return rating
    
    def extract_image_url(self, soup):
        image_url = ""
        return image_url
    

    

