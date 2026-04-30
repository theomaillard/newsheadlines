from .apnews import APNews
from .bbc import BBC
from .cnn import CNN
from .nyt import NYT
from .theguardian import TheGuardian

ALL_SOURCES: dict[str, type] = {
    "apnews": APNews,
    "bbc": BBC,
    "cnn": CNN,
    "nyt": NYT,
    "theguardian": TheGuardian,
}