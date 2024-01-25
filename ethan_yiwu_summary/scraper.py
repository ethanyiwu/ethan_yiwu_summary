## scraper.py
import requests
from bs4 import BeautifulSoup

class Scraper:
    def __init__(self, user_agent: str = 'Mozilla/5.0'):
        """
        Initialize the Scraper with a user agent.

        :param user_agent: The User-Agent string to be used for HTTP requests.
        """
        self.user_agent = user_agent

    def get_content(self, url: str) -> str:
        """
        Retrieve the content from the URL using a GET request and parse it with Beautiful Soup.

        :param url: The URL from which to scrape the content.
        :return: The text content of the page.
        """
        headers = {'User-Agent': self.user_agent}
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raises HTTPError if the HTTP request returned an unsuccessful status code

        # Parse the content using Beautiful Soup
        soup = BeautifulSoup(response.content, 'html.parser')
        return soup.get_text()

# Example usage:
# scraper = Scraper()
# content = scraper.get_content('http://example.com')
# print(content)
