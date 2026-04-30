import re

def clean_string(string: str):
    return re.sub(r'\s+', ' ', string).strip()




