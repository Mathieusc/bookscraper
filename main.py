import asyncio
from scripts.scraper import BookScraper
from logger.error_handler import setup_logging

async def main():
    setup_logging()

    book_url = "http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
    scraper = BookScraper(book_url)
    csv_filename = "data/book_data.csv"
    soup = await scraper.fetch_book_data()
    if soup:
        # Write the fetched book data inside BookSraper.book_data{}
        await scraper.scrape_and_extract(csv_filename)

if __name__ == "__main__":
    asyncio.run(main())
