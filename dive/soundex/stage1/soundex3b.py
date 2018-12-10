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
    digits2 = "".join([digits[i] for i in range(len(
        digits)) if i == 0 or digits[i] != digits[i-1]])
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

# 20 tests for 50000 each
# result of way 1a
# Woo             W000 0.44571715703
# Pilgrim         P426 0.479107457274
# Flingjingwaller F452 0.682555275898
# [Finished in 35.1s]
#
# result of way 2
#  Woo             0000 0.238047519682
#  Pilgrim         4265 0.248714139275
#  Flingjingwaller 4525 0.327573558541
#
# [Finished in 17.6s]
#
# result of way 3
#  Woo             W000 0.252284047445
#  Pilgrim         P426 0.297863597159
#  Flingjingwaller F452 0.413255870377
#
# [Finished in 21.2s]
# end of file
