import re

f = open('urls_6711', 'rb')
s = open('urls_6711_filtered', 'wb')


patterns = [
    r'ziliao\/\d+',
    r'bbs.*viewthread.php\?.+',
    r'news\/.+',
    r'bbs.*buddysubmit=yes',
]

for k in range(len(patterns)):
    patterns[k] = re.compile(patterns[k])


while True:
    l = f.readline()
    flag = False
    if not l:
        break
    for v in patterns:
        if v.search(l) is not None:
            flag = True
            break
    if flag:
        continue
    print(l),


f.close()
s.close()

#
