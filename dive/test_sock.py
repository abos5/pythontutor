# import
import os
from toolbox import exit


def fibonacci(max):
    a, b = 0, 1
    while a < max:
        yield a
        a, b = b, a + b
    return

for a in fibonacci(1000):
    print(a),
print('')

print("a" if True else exit())


def make_counter(x):
    print('entering make_counter')
    while 1:
        yield x
        print('incrementing x')
        x += 1

counter = make_counter(2)
counter
print(counter.next())
print(counter.next())

exit()
# file information

print(os.stat('rules.en'))



# end of file
