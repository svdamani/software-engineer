# Python 3 web crawler
from urllib.request import urlopen
from bs4 import BeautifulSoup
from sys import argv

# Scrape www.shopping.com
def scrape(keyword, page = None):
    url = 'http://www.shopping.com/products%s?KW=%s' % ((('~PG-%s' % page) if page else ''), keyword)
    soup = BeautifulSoup(urlopen(url), 'html.parser')
    if page == None:
        try:
            return soup.select_one('.numTotalResults').text.split()[-1]
        except:
        	return soup.select_one('.rtCol').h1.text
    else:
        return [span.text for span in soup.select('.quickLookGridItemFullName')]

if __name__ == '__main__':
    if len(argv) > 1:
        keyword = argv[1]
        page = int(argv[2]) if len(argv) > 2 else None
        print(scrape(keyword, page))