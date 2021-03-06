import string
import re

allchars = string.uppercase + string.lowercase
charToSoundex = string.maketrans(allchars, "91239129922455912623919292" * 2)
isOnlyChars = re.compile('^[A-Za-z]+$').search


def soundex(source):
    "convert string to Soundex equivalent"

    if not isOnlyChars(source):
        return "0000"
    digits = source[0].upper() + source[1:].translate(charToSoundex)
    digits2 = digits[0]
    for d in digits[1:]:
        if digits2[-1] != d:
            digits2 += d
    digits3 = ""
    for d in digits2:
        if d != '9':
            digits3 += d
    while len(digits3) < 4:
        digits3 += "0"
    return digits3[:4]


if __name__ == '__main__':
    from timeit import Timer
    names = ('Woo', 'Pilgrim', 'Flingjingwaller')
    print("\n#\n# result of way 2")
    for name in names:
        statement = "soundex('%s')" % name
        t = Timer(statement, "from __main__ import soundex")
        print("# "), (name.ljust(15)), (soundex(name)), (
            min(t.repeat(20, 50000)))
    print("# "),

# result of way 1 20 tests for 50000 each
# Woo             W000 0.44571715703
# Pilgrim         P426 0.479107457274
# Flingjingwaller F452 0.682555275898
# [Finished in 35.1s]
#
# result of way 2c
#  Woo             W000 0.245441039247
#  Pilgrim         P426 0.277628096524
#  Flingjingwaller F452 0.360868206922
#
# [Finished in 18.9s]
#
# result of way 2
#  Woo             W000 0.20227905959
#  Pilgrim         P426 0.248321679269
#  Flingjingwaller F452 0.303370763454
#
# [Finished in 16.4s]
# end of file
