import requests
from bs4 import BeautifulSoup
import csv
import time
import re

class BookScraper:
    """
    A class to scrape book data from 'Books to Scrape' website.
    """

    BASE_URL = "http://books.toscrape.com/catalogue/page-{}.html"
    GBP_TO_INR_RATE = 100  # Fixed conversion rate (1 GBP = 100 INR)

    def __init__(self, pages=5):
        """
        Initialize scraper with number of pages to scrape.
        :param pages: Number of pages to scrape
        """
        self.pages = pages
        self.books = []

    def fetch_page(self, page_number):
        """
        Fetch HTML content of a given page.
        :param page_number: page number to fetch
        :return: BeautifulSoup object of page content
        """
        url = self.BASE_URL.format(page_number)
        print(f"Fetching page {page_number}: {url}")
        try:
            response = requests.get(url)
            response.raise_for_status()
            return BeautifulSoup(response.text, 'html.parser')
        except requests.RequestException as e:
            print(f"Error fetching page {page_number}: {e}")
            return None

    def parse_book_data(self, book_soup):
        """
        Parse individual book information from the HTML snippet.
        :param book_soup: BeautifulSoup object of the book container
        :return: dictionary with book info
        """
        # Extract title
        title = book_soup.h3.a['title']

        # Extract price string like '£51.77' (may have encoding artifacts)
        price_text = book_soup.find('p', class_='price_color').text.strip()
        # Remove all characters except digits and dot to avoid encoding issues
        price_clean = re.sub(r'[^\d.]', '', price_text)
        price_gbp = float(price_clean)

        # Convert price to INR
        price_inr = price_gbp * self.GBP_TO_INR_RATE

        # Format price_inr as string with ₹ symbol and 2 decimals
        price_inr_str = f"₹{price_inr:.2f}"

        # Extract availability
        availability = book_soup.find('p', class_='instock availability').text.strip()

        # Extract rating (class names like "star-rating Three")
        rating_class = book_soup.find('p', class_='star-rating')['class']
        rating = self.convert_rating(rating_class[1])

        return {
            'title': title,
            'price_inr': price_inr_str,
            'availability': availability,
            'rating': rating
        }

    def convert_rating(self, rating_str):
        """
        Convert rating string to numeric value.
        :param rating_str: rating as string (One, Two, Three, Four, Five)
        :return: integer rating 1-5
        """
        ratings = {
            'One': 1,
            'Two': 2,
            'Three': 3,
            'Four': 4,
            'Five': 5
        }
        return ratings.get(rating_str, 0)

    def scrape_books(self):
        """
        Scrape books from all specified pages and collect data.
        """
        for page in range(1, self.pages + 1):
            soup = self.fetch_page(page)
            if soup is None:
                continue

            # Find all book containers
            book_list = soup.find_all('article', class_='product_pod')

            for book_soup in book_list:
                book_data = self.parse_book_data(book_soup)
                self.books.append(book_data)

            # Be polite and wait a bit
            time.sleep(1)

    def save_to_csv(self, filename='books_inr.csv'):
        """
        Save scraped book data to CSV file.
        :param filename: output filename
        """
        keys = ['title', 'price_inr', 'availability', 'rating']
        try:
            with open(filename, 'w', newline='', encoding='utf-8') as output_file:
                dict_writer = csv.DictWriter(output_file, fieldnames=keys)
                dict_writer.writeheader()
                dict_writer.writerows(self.books)
            print(f"Data saved to {filename}")
        except IOError as e:
            print(f"Error saving data to CSV: {e}")

def main():
    print("Starting book scraper...")
    scraper = BookScraper(pages=10)  # You can increase or decrease pages
    scraper.scrape_books()
    print(f"Scraped {len(scraper.books)} books.")
    scraper.save_to_csv()

if __name__ == '__main__':
    main()
