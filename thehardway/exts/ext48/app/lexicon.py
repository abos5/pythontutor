dictionary = {
    'direction': (
        'north', 'south', 'east', 'west', 'down',
        'up', 'left', 'right', 'back'),
    'verb': ('go', 'stop', 'kill', 'eat',),
    'stop': ('the', 'in', 'of', 'from', 'at', 'it',),
    'noun': ('door', 'bear', 'princess', 'cabinet',),
}


def scan(sentence):
    words = sentence.split(' ')
    results = []
    for word in words:
        results.append(translate_word(word))
    return results


def translate_word(word):
    global dictionary
    for key in dictionary:  # if is in dictionary
        if word.lower() in dictionary[key]:
            return (key, word)

    try:
        word = int(word)  # if is a number
        return ('number', word)
    except ValueError:
        return('error', word)  # error then

# end of file
