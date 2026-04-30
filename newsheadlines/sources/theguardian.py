from bs4 import BeautifulSoup
from ..base import Source
from ..models import Headline
from ..utils import clean_string
from ..caching import session

class TheGuardian(Source):
    name = "The Guardian"
    BASE_URL = "https://www.theguardian.com/international"

    def get_headlines(self) -> list[Headline]:
        
        r = session.get(self.BASE_URL)
        soup = BeautifulSoup(r.text, features="html.parser")
        headlines = []

        containers = soup.select('.dcr-dqlcr0')
        for c in containers: 
            prev_siblings_ids = [s.get('id') for s in c.find_previous_siblings()]
            if c.get('id') == "news" or "news" not in prev_siblings_ids:
                cards = c.select(".dcr-mwwxk")
                for card in cards:
                    headline = card.select_one(".dcr-uyefka")
                    title = clean_string(headline.get_text())

                    link = card.select_one("a")
                    url = "https://www.theguardian.com" + link.get("href")
                    
                    headlines.append(Headline(title=title, source=self.name, url=url))


        return headlines