import urllib2
import urllib
import cookielib
import os.path
import time
import config
import htmltool
import logging
import json

_opener = None
_required = {}


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
        ("Host", spy.site['host']),
        ("Origin", spy.site['domain_url']),
        ("Referer", spy.site['domain_url']),
        ("User-Agent", """Mozilla/5.0 (Windows NT 6.1; WOW64) ,Apple\
WebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36"""),
        ("X-Requested-With", "XMLHttpRequest"),
        ("X-Forwarded-For", "214.131.109.123"),
        ("Is-every-header-required", "I am awesome"),
    ]
    _opener.add_handler(htmltool.HTTPInternalError())
    # default handlers
    spy.opener = _opener
    return _opener


def satisfy_requirements(obj, requirements, prefix="require_"):
    """["c", ("a", ["b"]), "b"]
    require plugins
    """

    global _required
    for r in requirements:
        if isinstance(r, tuple):
            r, subr = r
            if not isinstance(subr, list):
                subr = [subr]
            satisfy_requirements(obj, subr, prefix)
        unique_key = str(obj)
        if unique_key not in _required.keys():
            _required[unique_key] = []
        if r in _required[unique_key]:
            continue
        method = getattr(obj, "%s%s" % (prefix, r))
        assert method(), "Require methods should return True if success."
        _required[unique_key].append(r)


class Spy(object):
    """Target:


    Memo:
    1. No need to close url sock, it's a pass method
    2. opener is where everything lands on
    3. req can use to help handler data and stuff
    4. opener.open return a response socket return by call chain
    5. call chain handlers http codes when they returns
    """
    def __init__(self):
        global _opener
        self.xsrf = None
        self.cookie = None
        self.site = config.site.copy()
        self.opener = _opener
        satisfy_requirements(self, self.site['core'])

    def require_opener(self):
        build_opener(self)
        return True

    def require_cookie(self):
        cookiefilepath = config.site['path']['cookie']
        # read cookie from file
        self.cookie = cookielib.MozillaCookieJar(cookiefilepath)
        self.cookie.load(ignore_discard=True)
        # refresh cookie valid date
        self.cookie.save(ignore_discard=True)
        cookieProcessor = urllib2.HTTPCookieProcessor(self.cookie)
        self.opener.add_handler(cookieProcessor)
        return True

    def require_xsrf(self):
        xsrffilepath = config.site['path']['xsrf']
        if not os.path.exists(xsrffilepath):
            open(xsrffilepath, 'w').close()
        fread = open(xsrffilepath, 'r')
        self.xsrf = fread.read()
        fread.close()
        flagRefresh = False
        timemodified = os.path.getmtime(xsrffilepath)
        if not self.xsrf:
            flagRefresh = True
        if time.time() - timemodified > config.site['xsrfexpired']:
            flagRefresh = True
        if flagRefresh:
            self.xsrf = self.request_xsrf()
        fwrite = open(xsrffilepath, 'w')
        fwrite.write(self.xsrf)
        fwrite.close()
        # could read an empty xsrf
        return True

    def require_login(self):
        now = time.time()
        for c in self.cookie:
            if c.is_expired(now):
                logging.info("Begin refresh login cookie")
                return self.request_login()
        logging.info("Use former cookie.")
        return True

    def request_xsrf(self):
        usock = self.opener.open(self.site['domain_url'])
        content = htmltool.handle_uscok(usock)
        parser = htmltool.ReadAttribute()
        parser.tag = self.site['parser_tag']
        parser.key = self.site['parser_key']
        parser.value = self.site['parser_value']
        parser.feed(content)
        parser.close()
        logging.info("found xsrf: %s" % parser.found)
        return parser.found

    def request_login(self):
        postdata = urllib.urlencode({
            self.site['xsrf_field']: self.xsrf,
            self.site['account_field']: self.site['account'],
            self.site['password_field']: self.site['password'],
            self.site['captcha_field']: self.site['captcha_field'],
        })
        usock = self.opener.open(self.site['login_url'], postdata)
        self.cookie.save(ignore_discard=True)
        # zipped content or uncode
        return usock.code == 200

    def run(self):
        """Store information that can be modified afterwards """
        satisfy_requirements(self, self.site['requirements'])
        request = Request(self.opener)
        request.feed(self.site['routes'])
        self.cookie.save(ignore_discard=True)
        return self  # don't break the chain


class Request(object):
    """docstring for Claws"""

    def __init__(self, opener):
        self.routes = None
        self.opener = opener

    def feed(self, routes):
        self.routes = routes
        for name, urls in routes:
            methodName = "request_%s" % name
            if hasattr(self, methodName):
                method = getattr(self, methodName)
            else:
                method = getattr(self, "unknown_request")
            if not isinstance(urls, list):
                urls = [urls]
            for url in urls:
                logging.info("Begin request %s" % name)
                method(url)
                logging.info("Done request %s" % name)

    def unknown_request(self, route):
        usock, content = self.open(route)
        print(content)
        return usock

    def request_nodeAnswerCommentBoxV2(self, route):
        return
        # make it a string
        params = json.dumps({'answer_id': '9812424', 'load_all': False})
        # url encode
        params = urllib.urlencode({'': params})
        url = "%s?params%s" % (route, params)
        usock = self.opener.open(url)
        result = htmltool.handle_uscok(usock)
        print(result)
        usock.close()

    def open(self, route):
        usock = self.opener.open(route)
        return (usock, htmltool.handle_uscok(usock))

    def request_people(self, route):
        result = self.open(route)
        print(result[1])

    def close(self):
        pass


# end of file
