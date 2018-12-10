import string
import re

charToSoundex = {
    "A": "9",
    "B": "1",
    "C": "2",
    "D": "3",
    "E": "9",
    "F": "1",
    "G": "2",
    "H": "9",
    "I": "9",
    "J": "2",
    "K": "2",
    "L": "4",
    "M": "5",
    "N": "5",
    "O": "9",
    "P": "1",
    "Q": "2",
    "R": "6",
    "S": "2",
    "T": "3",
    "U": "9",
    "V": "1",
    "W": "9",
    "X": "2",
    "Y": "9",
    "Z": "2"}


def soundex(source):
    "convert string to Soundex equivalent"

    allchars = string.uppercase + string.lowercase
    if not re.search("^[%s]+$" % allchars, source):
        return "0000"

    # Soundex algorithm:
    # 1. make first character uppercase

    source = source.upper()

    # 2. translate all other characters to Soundex digits
    digits = source[0] + "".join(map(lambda c: charToSoundex[c], source[1:]))

    # 3. remove consecutive duplicates
    digits2 = digits[0]
    for d in digits[1:]:
        if digits2[-1] != d:
            digits2 += d

    # 4. remove all "9"s
    digits3 = re.sub('9', '', digits2)

    # 5. pad end with "0"s to 4 characters

    while len(digits3) < 4:
        digits3 += "0"

    # 6. return first 4 characters
    return digits3[:4]


if __name__ == '__main__':
    from timeit import Timer
    names = ('Woo', 'Pilgrim', 'Flingjingwaller')
    print("\n# result of way 2")
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
# result of way 2
#  Woo             W000 0.394521652421
#  Pilgrim         P426 0.472973832852
#  Flingjingwaller F452 0.626513547054
# [Finished in 33.2s]
# end of file
