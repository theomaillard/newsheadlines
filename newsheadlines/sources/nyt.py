from bs4 import BeautifulSoup
from ..base import Source
from ..models import Headline
from ..utils import clean_string
from ..caching import session

class NYT(Source):
    name = "The New York Times"
    BASE_URL = "https://www.nytimes.com/"

    def get_headlines(self) -> list[Headline]:
        
        r = session.get(self.BASE_URL)
        soup = BeautifulSoup(r.text, features="html.parser")
        headlines = []

        # Main headline font degree: 1 (Largest) - 2 (Mid Large) - 3 (Large)
        # Degree 1
        if soup.select('.css-vidd8a'):
            card = soup.select_one('.css-8mz260')
            
            headline = card.select_one('.css-vidd8a')
            title = clean_string(headline.get_text())

            link = card.select_one('a.css-9mylee')
            url = link.get("href")

            headlines.append(Headline(title=title, source=self.name, url=url))
        
        # Degree 2
        elif soup.select('.css-1gulko'):
            card = soup.select_one('.css-acwcvw')

            headline = soup.select_one('.css-1gulko')
            title = clean_string(headline.get_text())

            link = card.select_one('a.css-9mylee')
            url = link.get("href")

            headlines.append(Headline(title=title, source=self.name, url=url))

        # Degree 3
        if soup.select('.css-1ixq7yl'):
            card = soup.select_one('.css-cfnhvx')

            headline = soup.select_one(".css-1ixq7yl")
            title = clean_string(headline.get_text())

            link = card.select_one("a.css-5mgoji")
            url = link.get("href")

            headlines.append(Headline(title=title, source=self.name, url=url))

        return headlines
    