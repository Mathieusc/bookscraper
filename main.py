import asyncio
from scripts.scraper import BookScraper
from logger.error_handler import setup_logging

async def main():
    # Set up logging
    setup_logging()

    book_url = "http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
    scraper = BookScraper(book_url)
    await scraper.fetch_book_data()

if __name__ == "__main__":
    asyncio.run(main())
