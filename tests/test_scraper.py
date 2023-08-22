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

def test_extract_price_excluding_tax():
    soup = BeautifulSoup(sample_html, "html.parser")
    book_scraper = BookScraper("http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html")
    result = book_scraper.extract_price_excluding_tax(soup)
    excepted_result = "£51.77"
    assert result == excepted_result

def test_extract_number_available():
    soup = BeautifulSoup(sample_html, "html.parser")
    book_scraper = BookScraper("http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html")
    result = book_scraper.extract_number_available(soup)
    excepted_result = "In stock (22 available)"
    assert result == excepted_result

def test_extract_product_description():
    soup = BeautifulSoup(sample_html, "html.parser")
    book_scraper = BookScraper("http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html")
    result = book_scraper.extract_product_description(soup)
    excepted_result = "It's hard to imagine a world without A Light in the Attic. This now-classic collection of poetry and drawings from Shel Silverstein celebrates its 20th anniversary with this special edition. Silverstein's humorous and creative verse can amuse the dowdiest of readers. Lemon-faced adults and fidgety kids sit still and read these rhythmic words and laugh and smile and love th It's hard to imagine a world without A Light in the Attic. This now-classic collection of poetry and drawings from Shel Silverstein celebrates its 20th anniversary with this special edition. Silverstein's humorous and creative verse can amuse the dowdiest of readers. Lemon-faced adults and fidgety kids sit still and read these rhythmic words and laugh and smile and love that Silverstein. Need proof of his genius? RockabyeRockabye baby, in the treetopDon't you know a treetopIs no safe place to rock?And who put you up there,And your cradle, too?Baby, I think someone down here'sGot it in for you. Shel, you never sounded so good. ...more"
    assert result == excepted_result

def test_extract_category():
    soup = BeautifulSoup(sample_html, "html.parser")
    book_scraper = BookScraper("http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html")
    result = book_scraper.extract_category(soup)
    excepted_result = "Poetry"
    assert result == excepted_result