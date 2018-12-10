# -*- coding: utf-8 -*-
#
import rediabos.conn  # the redis.Redis() instance
import rediabos.string  # basic get/set
import rediabos.string2  # basic get/set
import rediabos.hash  # basic get/set
import rediabos.hash2  # basic get/set
import rediabos.set  # with yield to loop over
import rediabos.set2  # with yield to loop over
import rediabos.zset  # not implemented now
import rediabos.zset2  # not implemented now

p = {
    'uname': 'Abos Freeman',
    'domain': 'http://www.yii2cms.com',
    'id': '123564897',
}

r = rediabos.conn

# =================================================
item = rediabos.string2(':people')
# available in string style method
# @return string, None(if failed)
item.set(100, p['uname']) is r.hset('people:1', '00', p['uname'])
item.get(100) is r.hget('people:1', '00')
# upgrade
item[100] = p['uname'] is item.set(100, p['uname'])
item[100] is item.get(100)
# if compression False
item.compression = False
item.set(100, p['uname']) is r.set('people:100', p['uname'])
item.get(100) is r.get('people:100')

# =================================================
item = rediabos.string('people')  # not supported to recommend style above
# item.set(p.uname) is r.set(p.uname)
# item.get() is r.get('people')

# =================================================
item = rediabos.hash('config', ('domain', 'seoOn'))
# simple hash
# @return string, None(if failed)
# @todo hash keys will have validation in the future
item.set('domain', p['uname']) is r.hset('config', 'domain', p['uname'])
item.get('domain') is r.hget('config', 'domain')

item['domain'] = p['domain'] is item.set('domain', p['domain'])
item['domain'] is item.get('domain')

# =================================================
item = rediabos.hash2(':profile', ('uname', 'id', 'thanks', 'ask'))
# 2d hash
# ":" is required
# .hset @return string, None(if failed)
# .hget @return string, None(if failed)
# .set @return string, None(if failed)
# .set @return string, None(if failed)
params = {'..': '..'}
for k, v in params.items():
    r.hset('profile:100', k, v)
item.set(100, params)  # is above
item.get(100) is rediabos.hash('profile:100')
item.hset(100, 'id', p['id']) is r.hset('profile:100', 'id', p['id'])
item.hget(100, 'id') is r.hget('profile:100', 'id')

item[100] is item.get(100)
item[100] = params is item.set(100, params)
item[100]['id'] is item.get(100)['id']
item[100]['id'] is item.get(100)['id']
item[100]['id'] is r.hget('profile:100', 'id')

# list/set
# =================================================
item = rediabos.madd('collected')
item = rediabos.set2(':collected')

# sorted list/set
item = rediabos.zset('collected')
item = rediabos.zset2(':collected')

r.save()  # save db from memory to disk


#
