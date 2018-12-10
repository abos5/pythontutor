# -*- coding: utf-8 -*-
"""not home test file
compare to test_kgp.py
"""

import sys
import urllib
from toolbox import exit, openAnything
from xml.dom import minidom
import httplib


_qqnewsxml = "http://news.qq.com/newsgn/rss_newsgn.xml"

# fsock = openAnything("qqnews.xml")
# contents = fsock.read()
# fsock.close()
_encodecounter = 0

contents = urllib.urlopen(_qqnewsxml).read()


httplib.HTTPConnection.debuglevel = 1
feeddata = urllib.urlopen("http://news.qq.com/newsgn/rss_newsgn.xml").read()
# print([feeddata])


# print(feeddata.encode('gb2312', 'ignore'))
exit()


def incredible_encode(c, codec=None):
    """should use this sequence:
    article to line to letter
    """
    global _encodecounter

    # write defualt here cause too long to be in args
    if codec is None:
        codec = [
            'Big5', 'GB2312', 'windows-1252',
            'HZ-GB-2312', 'ISO-8859-2', 'windows-1250',
            'ASCII', 'UTF-8', 'UTF-16', 'UTF-32', 'TIS-620',
            'ISO-8859-7', 'windows-1253', 'ISO-8859-8',
            'windows-1255', 'ISO-8859-1', 'koi8-r']
    _encodecounter += 1

    try:
        return c.encode(codec[0])
    except UnicodeDecodeError:
        if codec[1:] == []:
            return ""
        return incredible_encode(c, codec[1:])

newcontent = []
for c in contents:
    # escape from every thing
    break
    char = incredible_encode(c)
    newcontent.append(char)

print("".join(newcontent))
print(_encodecounter)
exit()
i = 0
for l in contents:
    line = str([l])
    if '\\x' in line:
        print(line)
        print(l.encode('ISO-8859-1'))
    if i > 200:
        break
    # if len(str([l])) > 1:
    #     print([l])
    i += 1

# print(contents[158].encode('gb2312'))
# print(contents.encode('gb2312'))


exit()


fsock = openAnything("binary.xml")
xmldoc = minidom.parse(fsock).documentElement

fsock.close()
print(xmldoc.getAttributeNS)
print(xmldoc.toxml())
exit()
print("\n".join(dir(xmldoc)))
exit()
i = 0
while False:
    sock = urllib.urlopen("http://www.yii2cms.com")
    htmlSource = sock.read()
    sock.close()
    if not i:
        break
    else:
        i -= 1
# fsock = open("test.html", "wb")
# fsock.write(htmlSource)
# fsock.close()

greeting = "hi"


def say():
    print(greeting)
print(sys.modules)
say()


print(globals())
