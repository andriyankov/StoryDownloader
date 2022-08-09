import requests


HEADERS = {
  'user-agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 OPR/80.0.4170.63',
  'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
}


def download_page(url):
  result = requests.get(url, headers=HEADERS)
  result.raise_for_status()
  return {'content': result.text, 'encoding': result.encoding}


def write_page(page, encoding, filename):
  with open(filename, 'wb') as f:
    f.write(page.encode(encoding))
