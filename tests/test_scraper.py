import pytest
from bs4 import BeautifulSoup
from .test_data import sample_html
from ..scripts.scraper import BookScraper

# Sample HTML content for testing, using a 'sample_html' singleton


def test_extract_universal_product_code():
    soup = BeautifulSoup(sample_html, "html.parser")
    book_scraper = BookScraper("http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html")
    result = book_scraper.extract_universal_product_code(soup)
    excepted_result = "a897fe39b1053632"
    assert result == excepted_result

def test_extract_title():
    soup = BeautifulSoup(sample_html, "html.parser")
    book_scraper = BookScraper("http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html")
    result = book_scraper.extract_title(soup)
    excepted_result = "A Light in the Attic"
    assert result == excepted_result

def test_extract_price_including_tax():
    soup = BeautifulSoup(sample_html, "html.parser")
    book_scraper = BookScraper("http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html")
    result = book_scraper.extract_price_including_tax(soup)
    excepted_result = "£51.77"
    assert result == excepted_result