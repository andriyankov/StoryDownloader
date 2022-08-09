from bs4 import BeautifulSoup
from .utils import download_page


def _parse_story_ids(html):
  soup = BeautifulSoup(html, 'lxml')
  tab = soup.find('img', attrs={'width': "100", 'height': "115"}).parent
  a_tags = tab.find_all(lambda t: t.has_attr('href') and 'sid=' in t.get('href'))
  links = sorted(set(a.get('href') for a in a_tags), reverse=True)
  if len(links) > 10:
    links.remove(min(links))
  for a in links:
    yield int(a.split('=')[1])


def get_stories_ids(host, pages_count):
  for n in range(pages_count):
    url = f'{host}?from={n*10}'
    html = download_page(url)['content']
    yield from _parse_story_ids(html)
