import sys, os
sys.path.insert(1, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import newsheadlines

def APNEWS():
    for news in newsheadlines.all('apnews'):
        print(news.title)
        print(news.url)

def BBC():
    for news in newsheadlines.all('bbc'):
        print(news.title)
        print(news.url)

def CNN():
    for news in newsheadlines.all('cnn'):
        print(news.title)
        print(news.url)

def NYT():
    for news in newsheadlines.all('nyt'):
        print(news.title)
        print(news.url)

def THEGUARDIAN():
    for news in newsheadlines.all('theguardian'):
        print(news.title)
        print(news.url)

if __name__ == "__main__":
    print("APNEWS")
    APNEWS()
    print()

    print("BBC")
    BBC()
    print()

    print("CNN")
    CNN()
    print()

    print("NYT")
    NYT()
    print()

    print("THEGUARDIAN")
    THEGUARDIAN()
