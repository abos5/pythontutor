print "Let's practive everything."
print 'You\'d need to know \'bout escapse with \\ that do \n new lines and \t tabs.'

poem = """
t The lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explaination
\n\t\t where there is none.
"""

print "------------------"
print poem
print "------------------"

five = 10 - 2 + 3 - 6
print "This should be five: %s" % five

def secret_fomula(started):
    jelly_beans = started * 50
    jars = jelly_beans / 1000
    crates = jars / 10
    return jelly_beans, jars, crates

start_point = 10000
beans, jars, crates = secret_fomula(start_point)

print "With a starting point of :%d" % start_point
print "We'd have %d beans, %d jars and %d crates." % (beans, jars, crates)

start_point = start_point / 10

print "We also do that this way:"
print "We'd have %d beans, %d jars and %d crates." % secret_fomula(start_point)
