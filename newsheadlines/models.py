from dataclasses import dataclass, asdict

@dataclass
class Headline:
    title: str
    source: str = ""
    url: str | None = None

    def to_dict(self) -> dict:
        return asdict(self)