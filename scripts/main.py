import asyncio
from scraper import BookScraper

async def main():
    book_url = "http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
    scraper = BookScraper(book_url)
    await scraper.fetch_book_data()

asyncio.run(main())
