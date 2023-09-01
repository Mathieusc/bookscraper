from bs4 import BeautifulSoup
import aiohttp
import asyncio
import csv
import re
import os
import sys
from logger.error_handler import log_error

class BookScraper:
    """
    Scraping book information from 'http://books.toscrape.com/' using
    Beautiful Soup.

    Attributes:
        book_url (str): URL of the book.
    """

    RATING_MAPPING = {
        "Zero": "0",
        "One": "1",
        "Two": "2",
        "Three": "3",
        "Four": "4",
        "Five": "5",
    }

    BASE_BOOK_URL = "http://books.toscrape.com/"

    def __init__(self, book_url):
        """
        Initialize the BookScraper object.

        Args:
            book_url (str): The URL of the book's page.
        """
        self.book_url = book_url
        self.book_data = {}

    async def scrape_and_extract(self, csv_filename):
        """
        Scrape book data and extract information.

        Args:
            csv_filename (str): The name of the CSV file to write to.
        """
        soup = await self.fetch_book_data()
        if soup:
            self.extract_book_info(soup)
            self.write_to_csv(csv_filename)

    async def fetch_book_data(self):
        """
        Fetch and parse the HTML content of the book's page.

        Returns:
            BeautifulSoup: The BeautifulSoup object representing the parsed
                           HTML.
        """
        async with aiohttp.ClientSession() as session:
            async with session.get(self.book_url) as response:
                html = await response.text()
                soup = BeautifulSoup(html, "html.parser")


                # DEBUG
                test = self.extract_product_page_url(soup)
                print(test)

        return soup

    def extract_book_info(self, soup):
        """
        Extract book information from the parsed HTML and store it in the
        book_data {} dictionary.
        """
        self.book_data["product_page_url"] = self.extract_product_page_url(soup)
        self.book_data["universal_product_code"] = self.extract_universal_product_code(soup)
        self.book_data["title"] = self.extract_title(soup)
        self.book_data["price_including_tax"] = self.extract_price_including_tax(soup)
        self.book_data["price_excluding_tax"] = self.extract_price_excluding_tax(soup)
        self.book_data["number_available"] = self.extract_number_available(soup)
        self.book_data["product_description"] = self.extract_product_description(soup)
        self.book_data["category"] = self.extract_category(soup)
        self.book_data["review_rating"] = self.extract_review_rating(soup)
        self.book_data["image_url"] = self.extract_image_url(soup)

    def extract_product_page_url(self, soup):
        """
        TO MODIFY LATER
        Get the book's URL.
        Use manual URL's for now but will loop through each book
        from each category later
        """

        return self.book_url
    
    def extract_universal_product_code(self, soup):
        """"
        Extract the Universal Product Code (UPC) of the book.

        Returns:
            str: The extracted UPC.
        """
        upc_element = soup.find("th", string="UPC")

        if upc_element:
            upc = upc_element.find_next_sibling()
            if upc:
                return upc.text
            else:
                log_error("UPC not found.")
        else:
            log_error("UPC element not found.")

        return None
    
    def extract_title(self, soup):
        """
        Extract the Title of the book.

        Returns:
            str: The book's title.
        """
        title = soup.find("h1")

        if title:
            return title.text
        else:
            log_error("Title not found.")

        return None
    
    def extract_price_including_tax(self, soup):
        """
        Extract the price including taxes of the book.

        Returns:
            str: The book's price with taxes.
        
        """
        price_with_tax = soup.find("th", string="Price (incl. tax)")

        if price_with_tax:
            price = price_with_tax.find_next("td")
            if price:
                return price.text
            else:
                log_error("Price not found.")
        else:
            log_error("Price including tax not found .")

        return None
    
    def extract_price_excluding_tax(self, soup):
        """
        Extract the price excluding taxes of the book.

        Returns:
            str: The book's price without taxes.
        """
        price_without_tax = soup.find("th", string="Price (excl. tax)")

        if price_without_tax:
            price = price_without_tax.find_next("td")
            if price:
                return price.text
            else:
                log_error("Price not found.")
        else:
            log_error("Price excluding tax not found.")

        return None
    
    def extract_number_available(self, soup):
        """
        Extract the number of books available.

        Returns:
            str: The book's number.
        """
        number_available = soup.find("p", {"class": "instock availability"})

        if number_available:
            return number_available.text.strip()
        else:
            log_error("Number available not found.")

        return None
    
    def extract_product_description(self, soup):
        """
        Extract the description of the book.

        Returns:
            str: The book's description.
        """
        description_heading = soup.find("h2", string="Product Description")

        if description_heading:
            description = description_heading.find_next("p")
            if description:
                return description.text
            else:
                log_error("Description not found.")
        else:
            log_error("Description heading not found.")

        return None
    
    def extract_category(self, soup):
        """
        Extract the category of the book.

        Returns:
            str: The book's category.
        """
        category_heading = soup.find("li", {"class": "active"})

        if category_heading:
            category = category_heading.find_previous_sibling()
            if category:
                return category.text.strip()
            else:
                log_error("Category not found.")
        else:
            log_error("Category heading not found.")

        return None
    
    def extract_review_rating(self, soup):
        """
        Extracts the review rating of the book.

        Returns:
            str: The book's rewiew rating.
        """
        rating_element = soup.find(class_=re.compile("^star-"))

        if rating_element:
            selected_rating_class = rating_element.attrs["class"][1]
            review_rating = self.RATING_MAPPING.get(selected_rating_class,
                                                    "Unknown")
        else:
            review_rating = "Not Found"
            log_error("Review rating not found in the provided soup")

        return review_rating
    


    def extract_image_url(self, soup):
        """
        Extract the image URL of the book.

        Returns:
            str: The image URL.
        """
        image_tag = soup.find("img")

        if image_tag:
            relative_image_url = image_tag.get("src")
            if relative_image_url:
                return self.build_absolute_image_url(relative_image_url)
            else:
                log_error("Image URL not found.")
        else:
            log_error("Image tag not found.")
            return None

    def build_absolute_image_url(self, relative_image_url):
        """
        Build the absolute image URL by appending the relative URL to the base
        book URL.

        Args:
            relative_image_url (str): The relative image URL.

        Returns:
            str: The absolute image URL.
        """
        if relative_image_url:
            absolute_image_url = self.BASE_BOOK_URL + relative_image_url.replace("../../", "")
            return absolute_image_url

        return None
    
    def write_to_csv(self, filename):
        """
        Write the extracted book information to a CSV file.

        Args:
            filename (str): The name of the CSV file to write to.
        """
        with open(filename, "w", newline="", encoding="utf-8") as csvfile:
            fieldnames = self.book_data.keys()
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerow(self.book_data)

