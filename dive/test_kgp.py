import sys
import kgp
import urllib

import StringIO
from xml.dom import minidom
# from kgp import KantGenerator

_debug = 1
d = {'id': 'foo'}
for k in d:
    print('%s["%s"] = %s' % ('d', k, d[k]))
# foo


def exit():
    if _debug:
        sys.exit()

################ stdout
ssock = StringIO.StringIO("c")
ssock.write('hi')
print(ssock.__doc__)
print(ssock.readlines())
ssock.close()
print('Dive in')
saveout = sys.stdout
fsock = open('out.log', 'a')
# sys.stdout = fsock
msg = "msg don't meed to invoke .write method directly."
saveout.write(msg)
print(msg)
# print('This message will be logged instead of displayed')
sys.stdout = saveout
fsock.close()
exit()
################ xml

# way no 1
# xmldoc = minidom.parse('binary.xml')
# way no 2

contents = '<grammar><ref id="bit"><p>0</p><p>1</p></ref></grammar>'
ssock = StringIO.StringIO(contents)
xmldoc = minidom.parse(ssock)
ssock.close()
print("StringIO: %s" % xmldoc.toxml())
fsock = open('binary.xml')
xmldoc = minidom.parse(fsock)
fsock.close()
print(xmldoc.toxml())
usock = urllib.urlopen("http://rss.slashdot.org/Slashdot/slashdot/to")
usock.close()
exit()
xmldoc = minidom.parse(usock)
# print(xmldoc.toxml())
xmldoc = minidom.parse('binary.xml')


reflist = xmldoc.getElementsByTagName('ref')
firstref = reflist[0]
plist = firstref.getElementsByTagName('p')
plist2 = xmldoc.getElementsByTagName('p')
print("plist %s " % plist)
print("plist2 %s " % plist2)

print(plist2[-1].parentNode)

print(reflist)
reattributes = reflist[0].attributes
print(reattributes.keys())
print(reattributes is reflist[0].attributes)
print('attributes: %s' % reattributes)
print('attributes: %s' % reflist[0].attributes['id'])
print('attributes: %s' % reflist[0].attributes['id'].value)
print(reflist[0].toxml())

exit()

x = 5
y = 6
x, y = (y, x)
print(x), (y)

exit()

xmldoc = minidom.parse('russiansample.xml')
title = xmldoc.getElementsByTagName('title')[0].firstChild.data
another = xmldoc.getElementsByTagName('another')[0].firstChild.data
# take a look at title in unicode
print([title])
print([another])
# convert it as we know
convertedtitle = title.encode('koi8-r')
convertedanother = another.encode('koi8-r')
# take a look at convertedtitle in koi8-r code
print([convertedtitle])
print([convertedanother])
# check printed result
print(convertedtitle)
print(convertedanother)


exit()

#

print(kgp)


rs = 1950 - 409 - 80
pad = 591
times = 2


print(rs, rs-(pad/times * (times-1)))

# end of file
