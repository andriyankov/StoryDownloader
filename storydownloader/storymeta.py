from bs4 import BeautifulSoup
from .utils import download_page


def _get_title(tab):
  return tab.find('h2').get_text()


def _get_categories(tab):
  atags = tab.find_all('p')[-2].find_all('a')
  return str([a.get_text() for a in atags])


def _get_parts_count(tab):
  atags = tab.find_all(lambda t: t.has_attr('href') and '[' in t.get_text())
  return 0 if len(atags) == 0 else int(atags[-1].get_text()[1:-1])


def _get_author(tab):
  atag = tab.find(lambda t: t.has_attr('href') and 'author=' in t.get('href'))
  return atag.get('href').split('=')[-1]


def _parse_meta(html):
  soup = BeautifulSoup(html, 'lxml')
  tab = soup.find('table', attrs={'width': '95%'})
  return {
    'author': _get_author(tab),
    'categories': _get_categories(tab),
    'parts_count': _get_parts_count(tab),
    'title': _get_title(tab)
  }


def get_story_meta(url):
  html = download_page(url)['content']
  return _parse_meta(html)
