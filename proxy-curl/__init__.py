import urllib2

import htmltool


_opener = None


def build_opener(spy, refresh=False):
    global _opener
    if not refresh and _opener:
        return _opener
    _opener = urllib2.build_opener(urllib2.HTTPHandler)

    """Set headers for every request.
    If a custom header for a certain request is required,
    define it using urllib2.Reqest
    """
    _opener.addheaders = [
        ("Accept", "*/*"),
        ("Accept-Encoding", "gzip,deflate"),
        ("Accept-Language", "zh-CN,zh;q=0.8,zh-TW;q=0.6,en;q=0.4"),
        ("Connection", "keep-alive"),
        ("Content-Type", "application/x-www-form-urlencoded;\
charset=UTF-8"),
        # ("Host", spy.site['host']),
        # ("Origin", spy.site['domain_url']),
        # ("Referer", spy.site['domain_url']),
        ("User-Agent", """Mozilla/5.0 (Windows NT 6.1; WOW64) ,Apple\
WebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36"""),
        ("X-Requested-With", "XMLHttpRequest"),
        # ("X-Forwarded-For", "214.131.109.123"),
        ("Is-every-header-required", "I am awesome"),
    ]
    _opener.add_handler(htmltool.HTTPInternalError())
    _opener.add_handler(htmltool.proxy_handler)
    # default handlers
    spy.opener = _opener
    return _opener


class Spy(object):
    def __init__(self):
        pass

spy = Spy()

build_opener(spy)

# usock = _opener.open("http://anypost.yii2cms.com")
usock = _opener.open("https://www.google.com")
result = htmltool.handle_uscok(usock)
print(result)
# end of file
