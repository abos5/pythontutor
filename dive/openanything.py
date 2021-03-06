"""Ultimate version of toolbox.openAnything
Open anything as a stream
"""
import sys
import urllib2
import urlparse
import gzip
from StringIO import StringIO

USER_AGENT = '/OpenAnything/1.0+Abos+Freeman'


class SmartRedirectHandler(urllib2.HTTPRedirectHandler):

    def http_error_301(self, req, fp, code, msg, headers):
        result = urllib2.HTTPRedirectHandler.http_error_301(
            self, req, fp, code, msg, headers)
        result.status = code
        return result

    def http_error_302(self, req, fp, code, msg, headers):
        result = urllib2.HTTPRedirectHandler.http_error_302(
            self, req, fp, code, msg, headers)
        result.status = code
        return result


class DefaultErrorHandler(urllib2.HTTPDefaultErrorHandler):

    def http_error_default(self, req, fp, code, msg, headers):
        result = urllib2.HTTPError(
            self, req, fp, code, msg, headers)
        result.status = code
        return result


def openAnything(source, etag=None, lastmodified=None, agent=USER_AGENT):
    """Url, filename or string -> stream

    Returned object is guaranteed
    to have all the basic stdio read methods (read, readline, readlines).
    Just .close() the object when you're done with it.

    If the etag argument is supplied, it will be used as the value of an
    If-None-Match request header.

    """

    if hasattr(source, 'read'):
        return source

    if source == '-':
        return sys.stdin

    if urlparse.urlparse(source)[0] == 'http':
        request = urllib2.Request(source)
        request.add_header('User-Agent', agent)
        if etag:
            request.add_header('If-None-Match', etag)
        if lastmodified:
            request.add_header('If-Modified-Since', lastmodified)

        request.add_header('Accept-encoding', 'gzip')
        opener = urllib2.build_opener(
            SmartRedirectHandler(), DefaultErrorHandler)
        return opener.open(request)

    try:
        return open(source)
    except (IOError, OSError):
        pass

    return StringIO(str(source))


def fetch(source, etag=None, last_modified=None, agent=USER_AGENT):
    """Fetch data and metadata from a URL, file, stream, or string"""
    result = {}
    f = openAnything(source, etag, last_modified, agent)
    result['data'] = f.read()
    if hasattr(f, 'headers'):
        result['etag'] = f.headers.get('ETag')
        result['lastmodified'] = f.headers.get('Last-Modified')
        if f.headers.get('content-encoding') == 'gzip':
            result['data'] = gzip.GzipFile(
                fileobj=StringIO(result['data'])).read()
    if hasattr(f, 'url'):
        result['url'] = f.url
        result['status'] = 200
    if hasattr(f, 'status'):
        result['status'] = f.status
    f.close()
    return result


# end of file
