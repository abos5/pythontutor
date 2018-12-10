import MySQLdb

connection = MySQLdb.connect(
    'db2.host', 'root', '3a7d30f2de', 'abostutor')


class QueryBase(object):
    cursor = None
    query = ""
    _data = None
    fetched = False

    def __init__(self, query):
        self.query = query

    def __enter__(self):
        self.cursor = connection.cursor()
        self.cursor.execute(self.query)
        return self

    @property
    def data(self):
        if not self.fetched:
            self._data = self.cursor.fetchall()
            self.fetched = True
        return self._data

    def __exit__(self, type, value, traceback):
        self.cursor.close()
        return isinstance(value, TypeError)




# eof
