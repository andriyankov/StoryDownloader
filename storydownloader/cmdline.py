import argparse


def parse_cmdline():
  parser = argparse.ArgumentParser('Stories downloader')
  parser.add_argument('-u', '--main-page-url', help='Main page URL', type=str, dest='main_page_url')
  parser.add_argument('-o', '--output-dir', help='Output directory', type=str, default='./output', dest='output_dir')
  return parser.parse_args()
