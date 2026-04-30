from requests_cache import CachedSession
from datetime import timedelta
import os
import tempfile


cache_path = os.path.join(tempfile.gettempdir(), "newsheadlines", "http_cache")
os.makedirs(os.path.dirname(cache_path), exist_ok=True)

session = CachedSession(
        cache_path, 
        backend='sqlite', 
        expire_after=timedelta(minutes=10)
    )
