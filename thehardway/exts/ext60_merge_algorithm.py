import random
from UserList import UserList


class BigFirstList(UserList):

    def __init__(self, value):
        UserList.__init__(self, value)
        self.sorted = {}

    def merge_sort(self):
        lt = self[:]
        _lt = []

        print(lt)

    def _merge_sort(self, source):
        unit_len = 6
        pos_last = min(unit_len, len(source))

        lt = source[:pos_last]
        _source = source[pos_last:]

        while True:
            pass

        return _source

    def _mer(self):
        pass


lt = BigFirstList([])
for i in range(100):
    if random.randint(0, 100) > random.randint(60, 100):
        lt.append(i)

lt.merge_sort()
