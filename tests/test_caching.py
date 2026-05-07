from newsheadlines.caching import session


def test_caching_works():
    session.cache.clear()
    test_url = "http://httpbin.org/get"

    response1 = session.get(test_url)
    assert not response1.from_cache

    response2 = session.get(test_url)
    assert response2.from_cache

