from bs4 import BeautifulSoup
from .utils import download_page


def get_pages_count(url):
  page = download_page(url)['content']
  soup = BeautifulSoup(page, 'html.parser')
  links = soup.find('font', color='#515151').parent.find_all('a')
  return int(links[:-3][-1].text[1:-1])
