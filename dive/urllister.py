
from sgmllib import SGMLParser
import urllib


class URLLister(SGMLParser):

    def reset(self):
        SGMLParser.reset(self)
        self.urls = []

    def start_a(self, attrs):
        href = [v for k, v in attrs if 'href' in k]
        if href:
            self.urls.extend(href)


usock = urllib.urlopen("http://news.qq.com/")
parser = URLLister()


def asy(parser, sock):
    print("start yield:"),
    yield parser.feed(sock.read())
    sock.close()
    parser.close()
    for url in parser.urls:
        print(url)
    return

nice = asy(parser, usock)

for n in nice:
    pass
print(2)
for n in nice:
    pass


# end of file
