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
