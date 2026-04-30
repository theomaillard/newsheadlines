from bs4 import BeautifulSoup
from itertools import takewhile
from ..base import Source
from ..models import Headline
from ..caching import session

class APNews(Source):
    name = "AP News"
    BASE_URL = "https://apnews.com/"


    def get_headlines(self) -> list[Headline]:
        
        r = session.get(self.BASE_URL)
        soup = BeautifulSoup(r.text, features="html.parser")
        headlines = []


        all_containers = soup.select(".TwoColumnContainer7030, .OneColumnContainer")
        main_containers = list(takewhile(
            lambda el: "TwoColumnContainer7030" in el.get("class", []),
            all_containers
        ))

        for container in main_containers:
            # array of 2 columns
            columns = container.select(".TwoColumnContainer7030-column")

            # for left column
            leftCol = columns[0]   
            pagelist = leftCol.select('.PageListStandardE')
            for box in pagelist:
                title = box.select_one('.PageListStandardE-leadPromo-info .PagePromoContentIcons-text').get_text()
                link = box.select_one('a.Link')
                url = link.get("href")

                headlines.append(Headline(title=title, source=self.name, url=url))
                
            # for right column  
            rightCol = columns[1]
            title = rightCol.select_one('.PageList-items-first .PagePromo-content .PagePromo-title .PagePromoContentIcons-text').get_text()
            link = box.select_one('a.Link')
            url = link.get("href")

            headlines.append(Headline(title=title, source=self.name, url=url))


        return headlines
