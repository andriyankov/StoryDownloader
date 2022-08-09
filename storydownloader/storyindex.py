import sqlite3


DB_SCHEME = '''CREATE TABLE IF NOT EXISTS stories
  (author TEXT,
  categories TEXT,
  id INTEGER UNIQUE_id INTEGER UNIQUE,
  title TEXT)
'''


class StoryIndex:
  def __init__(self, output_dir, filename='index.db'):
    connection = sqlite3.connect(f'{output_dir}/{filename}')
    with connection:    
      connection.execute(DB_SCHEME)
    self.__connection = connection

  def __del__(self):
    if self.__connection:
      self.__connection.close()

  def append(self, meta):
    values = [meta[k] for k in ('author', 'categories', 'id', 'title')]
    with self.__connection:
      query = 'INSERT INTO stories VALUES (?, ?, ?, ?)'
      self.__connection.execute(query, values)

  def is_downloaded(self, story_id):
    query = 'SELECT * FROM stories WHERE id = ?'
    with self.__connection:
      cur = self.__connection.execute(query, (story_id,))
      result = cur.fetchone() is not None
    return result

  def get_metas(self):
    with self.__connection:
      query = 'SELECT * FROM stories'
      cursor = self.__connection.execute(query)
      for meta in cursor:
        yield(meta)
