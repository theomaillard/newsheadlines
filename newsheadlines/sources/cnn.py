from bs4 import BeautifulSoup
from ..base import Source
from ..models import Headline
from ..utils import clean_string
from ..caching import session

class CNN(Source):
    name = "CNN"
    BASE_URL = "https://edition.cnn.com/"

    def get_headlines(self) -> list[Headline]:
        
        r = session.get(self.BASE_URL)
        soup = BeautifulSoup(r.text, features="html.parser")
        headlines = []

        stacks = soup.find_all('div', class_="stack")

        # main headline
        clickable_hl = stacks[1].select_one('.container__title_url-text')
        if clickable_hl is not None:
            link = stacks[1].select_one('.container__title-url')
            title = clean_string(clickable_hl.get_text())
            url = "https://edition.cnn.com/" + link.get("href")
            headlines.append(Headline(title=title, source=self.name, url=url))
        else:
            main_headline = stacks[1].select_one('.container__title')
            title = clean_string(main_headline.get_text())
            url = None
            headlines.append(Headline(title=title, source=self.name, url=url))
        
        # LEFT stack
        containers = stacks[0].select(".container")
        for cont in containers:
            cards = cont.select("li.card")
            for card in cards:
                link = card.select_one("a.container__link")
                # filter out videos headlines
                # if not link or link.get("data-link-type") == "video":
                #     continue

                title = card.select_one(".container__headline-text")
                if title:
                    title = clean_string(title.get_text())
                    url = "https://edition.cnn.com/" + link.get("href")
                    headlines.append(Headline(title=title, source=self.name, url=url))

        return headlines
    