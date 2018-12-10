# -*- coding: utf-8 -*-
# This lib only designed for scraping www.zhihu.com
"""
性能测试结果 (十万数据):
>>> users2 = {'username': 'foo bar', 'user_id': 'ABHIJKLMNOPRTUWYacegikm'}

>>> for x in range(100000):
>>>    conn.hmset('user:%s' % x,users2)
# time python test.py
real    0m6.722s
user    0m3.120s
sys     0m1.284s

>>> for x in range(100000):
>>>     fixture.users2[x] = users2
real    0m6.268s
user    0m3.027s
sys     0m1.169s


性能明显差异不大, 但多了字段限制功能
后期更能拓展 字段验证, 默认值 等等新功能,
不提高性能瓶颈, 提高开发效率

"""
from UserDict import UserDict
import collections

_conn = None


def build_conn(conn):
    global _conn
    _conn = conn


def hash_get_key_field(model, field):
    key = model.key + ":"
    field = str(field)
    size = model.size
    if len(field) > size:
        return {
            'key': key + field[:-size],
            'field': field[-size:]
        }
    else:
        return {'key': key, 'field': field}


def hash2_get_key(model, key):
    """model, key -> key
    model.key  # is model. prefix
    """
    return model.key % key


def list_get_index(i, length):
    if i >= length:
        raise ErrorOutofRange
    elif i >= 0:
        pass
    else:  # i < 0
        i = length + i
    return i


class String2(UserDict):
    """ preshard
    from string values to hash

    examples:
    >>> users = String2("users")
    >>> users[1001] = None

    >>> print(users[1001])

    """
    def __init__(self, key, size=2):
        UserDict.__init__(self)
        self.key = key
        self.size = size

    def __setitem__(self, field, value):
        return self.set(field, value)

    def __getitem__(self, field):
        return self.get(field)

    def __delitem__(self, field):
        key, field = hash_get_key_field(self, field)
        return _conn.hdel(key, field)

    def set(self, field, value):
        key, field = hash_get_key_field(self, field)

        if value is None:
            return _conn.hdel(key, field)

        return _conn.hset(key, field, value)

    def get(self, field):
        key, field = hash_get_key_field(self, field)
        return _conn.hget(key, field)


class Hash2(UserDict):
    """ just a simple hash

    """
    def __init__(self, key, fields):
        UserDict.__init__(self)
        self.key = "%s:%s" % (key, "%s")
        self.fields = fields

    def __setitem__(self, key, values):
        return self.set(key, values)

    def __getitem__(self, key):
        return self.get(key)

    def __delitem__(self, key):
        return self.delete(key)

    def hset(self, key, field, value):
        """set a field
        """
        return self.get(key).set(field, value)

    def hget(self, key, field):
        """get a field
        """
        return self.get(key).get(field)

    def hdel(self, key, field):
        """del a field
        """
        return self.get(key).delete(field)

    def set(self, key, values):
        """set a dict
        """
        self._validate_fields(values.keys())
        return _conn.hmset(hash2_get_key(self, key), values)

    def get(self, key):
        """get a dict
        """
        full_key = hash2_get_key(self, key)
        hashdict = Hash(full_key, self.fields)
        return hashdict

    def delete(self, key):
        """delete a dict
        """
        return _conn.delete(hash2_get_key(self, key))

    def _validate_fields(self, fields):
        for field in fields:
            if field not in self.fields:
                raise (ErrorInvalidHashField)
        return True


class Hash(UserDict):
    """ hash

    """
    def __init__(self, key, fields):
        UserDict.__init__(self)
        self.key = key
        self.fields = fields
        self.data = _conn.hgetall(self.key)
        data_keys = self.data.keys()
        for field in fields:
            if field not in data_keys:
                self.data[field] = None

    def __setitem__(self, field, value):
        return self.set(field, value)

    def __getitem__(self, field):
        return self.get(field)

    def __delitem__(self, field):
        return self.delete(field)

    def set(self, field, value):
        self._validate_field(field)
        self.data[field] = value
        if value is None:
            return _conn.hdel(self.key, field)

        return _conn.hset(self.key, field, value)

    def get(self, field):
        self._validate_field(field)
        self.data[field] = _conn.hget(self.key, field)
        return self.data[field]

    def delete(self, field):
        self._validate_field(field)
        del self.data[field]
        return _conn.hdel(self.key, field)

    def _validate_field(self, field):
        if field not in self.fields:
            raise (ErrorInvalidHashField)
        return True


# List
# Enum
# Sort


class List(collections.MutableSequence):
    """Docstring for List
    Can't known if element exists.
    """
    def __init__(self, key):
        self.key = key
        self.data = []

    def __repr__(self):
        return _conn.lrange(self.key, 0, -1)

    def __len__(self):
        return _conn.len(self.key)

    def __getitem__(self, i):
        return _conn.lindex(self.key, i)

    def __setitem__(self, i, item):
        return _conn.lset(self.key, i, item)

    def __delitem__(self, i):
        return self.delete(i)

    def __getslice__(self, i, j):
        i = max(i, 0)
        j = max(j, 0)
        return _conn.lrange(self.key, i, j)

    def __setslice__(self, i, j, other):
        length = len(other)
        llen = _conn.llen(self.key)
        i = list_get_index(i, llen)
        j = list_get_index(j, llen)
        counter = 0
        sliced = j - i
        _conn.ltrim(self.key, i, j)
        # _conn.linsert(self.key, i, )
        return other

    def __delslice__(self, i, j):
        i = max(i, 0)
        j = max(j, 0)
        return _conn.ltrim(self.key, i, j)

    def __add__(self, other):
        return _conn.lpush(self.key, *other)

    def __radd__(self, other):
        return _conn.rpush(self.key, *other)

    def __iadd__(self, other):
        return _conn.rpush(self.key, *other)

    def set(self, i, item):
        return _conn.lset(self.key, i, item)

    def append(self, item):
        return _conn.lpush(self.key, item)

    def push(self, item):
        return _conn.rpush(self.key, item)

    def pop(self):
        return _conn.rpop(self.key)

    def remove(self, item):
        return _conn.lrem(self.key, item, 0)

    def count(self):
        return _conn.llen(self.key)

    def index(self, item, *args):
        raise NotImplementedError

    def reverse(self):
        raise NotImplementedError

    def sort(self, *args, **kwds):
        raise NotImplementedError

    def extend(self, other):
        raise NotImplementedError

    def __str__(self):
        return str(_conn.lrange(self.key, 0, -1))

    def insert(self, i, item):
        raise NotImplementedError
        if (_conn.llen(self.key) <= i):
            raise ErrorOutofRange
        return _conn.linsert(self.key, 'BEFORE', i, item)

    def __mul__(self, n):
        raise NotImplementedError

    __rmul__ = __mul__

    def __imul__(self, n):
        raise NotImplementedError

    def __lt__(self, other):
        raise NotImplementedError

    def __le__(self, other):
        raise NotImplementedError

    def __eq__(self, other):
        raise NotImplementedError

    def __ne__(self, other):
        raise NotImplementedError

    def __gt__(self, other):
        raise NotImplementedError

    def __ge__(self, other):
        raise NotImplementedError

    def __cast(self, other):
        raise NotImplementedError

    def __cmp__(self, other):
        raise NotImplementedError

    def __contains__(self, item):
        raise NotImplementedError

    __hash__ = None  # Mutable sequence, so not hashable


class ErrorInvalidHashField(Exception):
    pass


class ErrorOutofRange(Exception):
    pass


#
