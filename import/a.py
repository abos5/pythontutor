print "a before b"
import b
print "a after import b"


_once = 0


def dofoo():
    global _once;
    _once += 1
    if _once > 1:
	print "what the hell are u thinking?"
    print "a very important function that can only exec once"

dofoo()

print "complete a"
