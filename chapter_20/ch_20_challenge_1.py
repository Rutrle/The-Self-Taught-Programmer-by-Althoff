import urllib.request
from bs4 import BeautifulSoup
import os


class Scraper:

    def __init__(self, site):
        self.site = site

    def scrape(self):
        r = urllib.request.urlopen(self.site)
        html = r.read()
        parser = "html.parser"
        articles = []
        sp = BeautifulSoup(html, parser)
        for tag in sp.find_all("a"):

            url = tag.get("href")
            # print(url)

            if url is None:
                continue
            if "html" in url:
                print("\n"+url)
                articles.append(url)

        return articles


news = "https://www.novinky.cz/"
articles = Scraper(news).scrape()

print

directory = os.getcwd()

with open(os.path.join(directory, "chapter_20", "news.txt"), "w") as f:
    for article in articles:
        f.write(article)
        f.write('\n')
