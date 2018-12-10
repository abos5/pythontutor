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
    return (digits2.replace('9', '') + "000")[:4]


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
#
# result of way 2
#  Woo             W000 0.148327303434
#  Pilgrim         P426 0.165006853682
#  Flingjingwaller F452 0.229197464446
#
# [Finished in 11.8s]
#
# result of way 2
#  Woo             W000 0.11870683607
#  Pilgrim         P426 0.159892557916
#  Flingjingwaller F452 0.227281142995
#
# [Finished in 10.8s]
#
# result of way 2
#  Woo             W000 0.114241166674
#  Pilgrim         P426 0.157122759109
#  Flingjingwaller F452 0.220305125339
#
# [Finished in 10.5s]
# end of file
