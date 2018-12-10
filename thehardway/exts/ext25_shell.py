import ext25

sentence = "All good things come to those who wait."

words = ext25.break_words(sentence)
print words

sorted_words = ext25.sort_words(words)
print sorted_words

ext25.print_first_word(words)
ext25.print_last_word(words)

#wrods
print words

print "----\nprinting first word:"
ext25.print_first_word(sorted_words)

print "----\nprinting last word:"
ext25.print_last_word(sorted_words)

print "----\nprinting first and last word:"
ext25.print_first_and_last(sentence)

print "----\nprinting first and last sorted word:"
ext25.print_first_and_last_sorted(sentence)

help(ext25)