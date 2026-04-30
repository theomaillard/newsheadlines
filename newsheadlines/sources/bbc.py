from bs4 import BeautifulSoup
from ..base import Source
from ..models import Headline
from ..utils import clean_string
from ..caching import session

class BBC(Source):
    name = "BBC News"
    BASE_URL = "https://www.bbc.com/news"

    def get_headlines(self) -> list[Headline]:

        r = session.get(self.BASE_URL)
        soup = BeautifulSoup(r.text, features="html.parser")
        headlines = []

        # special top news
        top_event_container = soup.find("section", {"data-testid": "connecticut-grid-1"})
        if top_event_container:
            title = clean_string(top_event_container.select_one(".sc-feaf8701-3").get_text())
            link = top_event_container.select_one("a")["href"]
            if link.startswith("https://www.bbc.com"):
                url = link
            else:
                url = "https://www.bbc.com" + link

            headlines.append(Headline(title=title, source=self.name, url=url))

        # normal news
        container = soup.find("section", {"data-testid": "virginia-grid-8"})

        top_banner = container.find('div', class_="sc-82b3c53b-0 OpcHF")
        bot_banner = container.find('div', class_="sc-82b3c53b-0 kIJWJi")
        col = container.find('div', class_="sc-82b3c53b-0 cKhECM")

        to_parse = [top_banner, bot_banner, col]
        for item in to_parse:
            titles = item.select(".sc-feaf8701-3")
            if item is top_banner:
                links = [item.select_one("a")["href"]]
            else:
                links = [a["href"] for a in item.select("a")]
            
            for hl, lk in zip(titles, links):
                title = clean_string(hl.get_text())

                if lk.startswith("https://www.bbc.com"):
                    url = lk    
                else:
                    url = "https://www.bbc.com" + lk

                headlines.append(Headline(title=title, source=self.name, url=url))

        horizontal_banner = soup.find("div", {"data-testid": "ohio-grid-5"})
        cards = horizontal_banner.select(".sc-225578b-0")
        links = [a["href"] for a in horizontal_banner.select("a")]

        for hl, lk in zip(cards, links):
            title = clean_string(hl.select_one(".sc-feaf8701-3").get_text())
            url = "https://www.bbc.com" + lk
            headlines.append(Headline(title=title, source=self.name, url=url))

        return headlines
    