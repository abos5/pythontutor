# -*- coding: utf-8 -*-
# from UserDict import UserDict
# UserDict('a')

import sys
import fixture

users = fixture.users  # Hash
users2 = fixture.users2  # Hash2
userids = fixture.userids  # String2
founder_names = fixture.founder_names
# delete trash
# for x in range(100000):
#     fixture.conn.delete("user:%s" % x)

# for x in range(100000):
#     fixture.conn.hmset(
#         'user:%s' % x,
#         fixture.data['users2'][0]
#     )

# print(users2[2])

# for x in range(100000):
#     fixture.users2[x] = fixture.data['users2'][0]
# sys.exit()

# define a redis model
rstr = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789_"


def test_set_userids():
    for x in range(1000):
        userids[x] = rstr[:x % 64]


def test_read_userids():
    for x in range(1000):
        print(userids[x])

# users[1001] = None


def do_userids():
    print(type(userids[1001]))
    print(type(userids[1003]))
    del userids[1001]


def do_users():
    # users['username'] = 'foo bar'
    # users['user_id'] = userids[1]
    print(userids[1])
    print(users['username'])
    print(users['user_id'])


def do_users2():
    # users2[1]['username'] = 'foo bar'
    # users2[1]['user_id'] = userids[1]
    users2[2]['username'] = 'foo bar'
    print(users2[2])
    print(users2[1])


def do_founder_names():
    # founder_names[0] = -2
    # founder_names.push(1)
    # founder_names.pop()
    # print(founder_names)
    # founder_names[:] = [1]
    founder_names[0:1] = [-1, 2, 3]
    # print(founder_names[3:])
    print(founder_names)

do_founder_names()
# test_set_userids()
# do_users()
# do_users2()

#
