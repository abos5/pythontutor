# -*- coding: utf-8 -*-

import rediabos
import redis
import settings

conn = redis.Redis(**settings.conn)
rediabos.build_conn(conn)

userids = rediabos.String2("userid")
user = rediabos.Hash("user", ('username', 'user_id'))
users = rediabos.Hash2("user", ('username', 'user_id'))
founder_names = rediabos.List("founder_names")


data = {
    'users2': [
        {
            'username': 'foo bar',
            'user_id': 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklm',
            # 'hacked': 'haha',
        },
    ],
}


#
