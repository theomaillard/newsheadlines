from .sources import ALL_SOURCES

def all(source_name: str = None):
    if source_name.lower() in ALL_SOURCES:
        source_class = ALL_SOURCES[source_name]
        return source_class().get_headlines()
    else:
        raise ValueError("Wrong arguments inserted..")
    
def main(source_name: str):
    if source_name.lower() in ALL_SOURCES:
        source_class = ALL_SOURCES[source_name]
        return source_class().get_main_headline()
    else:
        raise ValueError("Wrong arguments inserted..")