import pytest

import newsheadlines
from newsheadlines.sources import ALL_SOURCES
from newsheadlines.models import Headline


@pytest.mark.parametrize("source", ALL_SOURCES.keys())
def test_source_returns_all_headlines(source):
    headlines = newsheadlines.all(source)
    assert headlines
    for headline in headlines:
        assert isinstance(headline, Headline)


@pytest.mark.parametrize("source", ALL_SOURCES.keys())
def test_source_returns_main_headline(source):
    headline = newsheadlines.main(source)
    assert headline
    assert isinstance(headline, Headline)