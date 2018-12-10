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
    digits3 = re.sub('9', '', digits2)
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
# result of way 2a
#  Woo             W000 0.394521652421
#  Pilgrim         P426 0.472973832852
#  Flingjingwaller F452 0.626513547054
# [Finished in 33.2s]
#
# result of way 2b
#  Woo             W000 0.370683812297
#  Pilgrim         P426 0.432303317395
#  Flingjingwaller F452 0.554885901285
#
# [Finished in 29.7s]
#
# result of way 2c
#  Woo             W000 0.242933975172
#  Pilgrim         P426 0.27535503057
#  Flingjingwaller F452 0.364904879764
#
# [Finished in 18.9s]
# end of file
