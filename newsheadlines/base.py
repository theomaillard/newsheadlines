from abc import ABC, abstractmethod
from .models import Headline


class Source(ABC):
    name: str = ""
    BASE_URL: str = ""

    @abstractmethod
    def get_headlines(self) -> list[Headline]:
        raise NotImplementedError

    def get_main_headline(self) -> Headline:
        return self.get_headlines()[0]
