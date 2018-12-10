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

isOnlyChars = re.compile("^[a-zA-Z]+$").search


def soundex(source):
    "convert string to Soundex equivalent"

    if not isOnlyChars(source):
        return "0000"

    # Soundex algorithm:
    # 1. make first character uppercase

    source = source[0].upper() + source[1:]

    # 2. translate all other characters to Soundex digits
    digits = source[0]  # string
    for s in source[1:]:
        s = s.upper()
        digits += charToSoundex[s]

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
    for name in names:
        statement = "soundex('%s')" % name
        t = Timer(statement, "from __main__ import soundex")
        print(name.ljust(15)), (soundex(name)), (min(t.repeat(20, 50000)))

# 20 tests for 50000 each
# result of way 1
# Woo             W000 0.44571715703
# Pilgrim         P426 0.479107457274
# Flingjingwaller F452 0.682555275898
# [Finished in 35.1s]
# Woo             W000 0.347424399107
# Pilgrim         P426 0.480323836978
# Flingjingwaller F452 0.67085988562
# [Finished in 33.1s]
# Woo             W000 0.30222376214
# Pilgrim         P426 0.381320874233
# Flingjingwaller F452 0.654043631207
# [Finished in 28.0s]
# end of file
