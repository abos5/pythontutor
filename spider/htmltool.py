#  This module proves its value,
#  I am moving it to a system wide level to make sure it gets a cano
from sgmllib import SGMLParser
import StringIO
import gzip
import urllib2


class ReadAttribute(SGMLParser):

    def reset(self):
        self.attrs = {}
        self.tag = False
        self.key = False
        self.value = False
        self.found = False
        SGMLParser.reset(self)

    def unknown_starttag(self, tag, attrs):

        assert self.tag and self.key and self.value, "Values should be defined"

        if tag != self.tag or self.found:
            return
        a = {}
        flagfound = False
        for name, value in attrs:
            a[name] = value
            if (name, value) == self.key:
                flagfound = True
        if flagfound:
            self.found = a[self.value]


class HTTPInternalError(urllib2.BaseHandler):

    def http_error_500(self, req, fp, code, msg, headers):
        import logging
        logging.error('error requesting url: %s' % msg)


def handle_uscok(usock):
    compressedresult = usock.read()
    result = compressedresult
    flagGzip = False
    flagJson = False

    for k, v in usock.headers.items():
        if (k, v) == ("content-encoding", "gzip"):
            flagGzip = True
        if (k, v) == ("content-type", "application/json"):
            flagJson = True
        if flagGzip and flagJson:
            break

    if flagGzip:
        compressedstream = StringIO.StringIO(compressedresult)
        gzipper = gzip.GzipFile(fileobj=compressedstream)
        result = gzipper.read()
        compressedstream.close()
        gzipper.close()

    if flagJson:
        import json
        result = json.loads(result)

    return result


def modify_cookie():
    f = open(config.site['path']['cookie'], 'r')
    for l in f:
        if "#" in l and l.index("#") == 0:
            continue
        words = l.split('\t')
        domain, domain_specified, path, secure, expires, name, value = words
        del words, l

        print(domain, domain_specified, path, secure, expires, name, value)
    exit()
    # domain, domain_specified, path, secure, expires, name, value
    cookies = [
        [
            "www.zhihu.com", "FALSE", "/", "FALSE", "",
            "_xsrf", "c28ec8ec128d530065bf16d5f4430cc8"],
        [
            "www.zhihu.com", "FALSE", "/", "FALSE",
            "", "c_c", "de6aaa128ea811e489645254291c3363"],
        [
            ".zhihu.com", "TRUE", "/", "FALSE", "", "q_c0", "\"MWM1Y2E4MmVlMTViMTI2NWUyOTRiZGI0NTE3NGNiOGV8YTNadEd6d0JOTTJjUDk2ZA==|1419781671|28a69e11f44ed67a2d4c810a1cae56ea670b7d6b\""],
        [
            ".zhihu.com", "TRUE", "/", "FALSE", "", "q_c1", "f4d55dcc4af340958226153e1aedeb9b|1419781666000|1419781666000"]
    ]
    f = open(config.site['path']['cookie'], 'a')
    for l in cookies:
        f.write("\t".join(l))
        f.write("\n")
    f.close()


proxy_handler = urllib2.ProxyHandler({"http": '114.215.109.253:80'})
proxy_handler = urllib2.ProxyHandler({"http": '127.0.0.1:80'})


# end of file
