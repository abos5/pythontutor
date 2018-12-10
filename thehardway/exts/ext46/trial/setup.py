try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Abos Freeman',
    'author': 'Abos Freeman',
    'url': 'http://www.yii2cms.com/some_where',
    'download_url': 'file://data/python/tutor/thehardway/exts/ext46/skeleton/',
    'author_email': 'abos.freeman@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['app'],
    'scripts': [],
    'name': 'trial'
}

setup(**config)
