from bs4 import BeautifulSoup
from .utils import download_page
from .utils import write_page


def _parse_content(html):
  soup = BeautifulSoup(html, 'lxml')
  tab = soup.find('table', attrs={'width': '95%'})
  for p in tab.find_all('p')[1:-2]:
    if (p.find(['a', 'i'])):
      continue
    for br in p.find_all('br'):
      br.replace_with('\n')
    text = p.get_text().strip()
    if text:
      yield(text.replace('\r\n', ' ').replace('\t', ''))


def _parse_story(url, parts_count):
  html = download_page(url)['content']
  result = ''
  for p in _parse_content(html):
    result += (p+'\n\n')
  for i in range(2, parts_count+1):
    html = download_page(f'{url}&part={i}')['content']
    for p in _parse_content(html):
      result += (p+'\n\n')
  return result


def download_story(url, meta, output_dir):
  story = _parse_story(url, meta['parts_count'])
  write_page(story, 'utf-8', f'{output_dir}/{meta["id"]}.txt')
