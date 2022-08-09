import sys
from .errors import ApplicationError
from .startpage import get_pages_count
from .storyid import get_stories_ids
from .storymeta import get_story_meta
from .story import download_story
from .storyindex import StoryIndex
from .cmdline import parse_cmdline


def main(main_page_url, output_dir):
  try:
    pages_count = get_pages_count(main_page_url)
    stories_ids = get_stories_ids(main_page_url, pages_count)
    index = StoryIndex(output_dir)
    page_no = 0
    for story_id in stories_ids:
      if index.is_downloaded(story_id):
        print(f'Story with ID "{story_id}" already downloaded')
        continue
      url = f'{main_page_url}/read.php?sid={story_id}'
      meta = get_story_meta(url)
      meta['id'] = story_id
      download_story(url, meta, output_dir)
      index.append(meta)
      print(f'Story with ID "{story_id}" saved')
      page_no += 1
      if page_no % 10 == 0:
        print(f'{page_no} stories of ~{pages_count*10} parsed')
  except ApplicationError as e:
    print(e, file=sys.stderrr)


args = parse_cmdline()
main(args.main_page_url, args.output_dir)
