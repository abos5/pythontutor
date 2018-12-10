# import os.path
from os import path
import logging

debug = 1
author = 'Abos'
rootpath = path.abspath(path.join(path.dirname(__file__), './../'))
downloadpath = path.join(rootpath, 'downloads')
paths = [
    ("root", "./"),
    ("download", downloadpath),
    ("test", 'test'),
    ("config", 'config'),
]
_zhihu = {
    'name': 'zhihu',
    'domain_url': 'http://www.zhihu.com',
    'login_url': 'http://www.zhihu.com/login',
    'host': 'www.zhihu.com',
    'account': '********',
    'password': '********',
    'account_field': 'email',
    'password_field': 'password',
    'parser_tag': 'input',
    'parser_key': ('name', '_xsrf'),
    'parser_value': 'value',
    'xsrf_field': '_xsrf',
    'require_xsrf': True,
    'require_login': True,
    'xsrfexpired': 18000,
    'path': [
        ('runtime', 'runtime'),
        ('xsrf', 'runtime/xsrf.txt'),
        ('cookie', 'runtime/cookie.txt'),
        ('log', 'runtime/application.log'),
    ],
    'routes': [
        # ('test', ['/']),
        # ('test', '/'),
        # ('nodeAnswerCommentBoxV2', '/node/AnswerCommentBoxV2'),
        # ('collections', '/collection/20279745'),
        ('people', '/people/wonderful-vczh'),
    ],
    'core': ['opener'],
    'requirements': [('login', ['cookie']), 'xsrf']  # "xsrf",
}
_anypost = {
    'name': 'anypost',
    'domain_url': 'http://anypost.yii2cms.com',
    'login_url': 'http://anypost.yii2cms.com/site/login',
    'host': 'anypost.yii2cms.com',
    'account': '********',
    'password': '********',
    'account_field': 'LoginForm[username]',
    'password_field': 'LoginForm[password]',
    'captcha_field': '',
    'xsrf_field': '',
    'require_xsrf': False,
    'require_login': True,
    'require_cookie': True,
    'xsrfexpired': 600,
    'path': [],
    'routes': [
        ('admin', ['/anypost/admin']),
    ],
    'core': ['opener'],
    'requirements': [('login', ['cookie'])]  # "xsrf",
}

# site = _anypost
site = _zhihu


def abspath(paths, parentdir=""):
    _path = {}
    for n, p in paths:
        _p = p
        if not path.abspath(p) == p:
            _p = path.join(parentdir, p)
        _p = path.realpath(path.abspath(_p))
        _path[n] = _p
    return _path


def absroute(routes, parenturl=""):
    _routes = []
    for n, r in routes:
        if not isinstance(r, list):
            r = [r]
        _r = [parenturl + u for u in r]
        _routes.append((n, _r))
    return _routes

site['routes'] = absroute(site['routes'], site['domain_url'])

site['path'] = abspath(site['path'], path.join(downloadpath, site['name']))
paths = abspath(paths)

loggingConfig = {
    "filename": site['path']['log'],
    "format": "%(asctime)-15s:%(name)s:%(levelname)s %(message)s",
    "level": logging.INFO,
}
logging.root = logging.getLogger(author)
logging.basicConfig(**loggingConfig)
logging.info("config complete")
import spy
Spy = spy.Spy
# end of file
