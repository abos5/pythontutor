types = {'f': {}, 's': {}, 'd': {}, 'r': {}}

var = {'f': {}, 's': {}, 'd': {}, 'r': {}}
var['d']['1'] = 100
var['f']['2'] = 234.456789
var['s']['3'] = "234.456789"
var['s']['4'] = '234.456789'
var['s']['5'] = '''234.456789'''
var['d']['6'] = -222
var['d']['7'] = 123


fs = {'f': {}, 's': {}, 'd': {}, 'r': {}}
fs['f']['1'] = "% 15.3f"
fs['f']['2'] = "% 15f"
fs['f']['3'] = "%-f"
fs['f']['4'] = "%-16f"
fs['f']['5'] = "%16f"
fs['f']['6'] = "%+ 16f"
fs['f']['7'] = "% +f"
fs['f']['8'] = "%+ 16f"
fs['s']['9'] = "%+ 16r"

for t in types:
    
    for v in var[t]:
        for f in fs[t]:
            print "type [%2s] format [%-8s] variable [%12s]: %s" % (
                t,
                fs[t][f],
                var[t][v],
                fs[t][f] % var[t][v]
            )


'''
print "%#x" % num1

# "%m.nf" returns a str with at least m width, firm n digits after '.'
print "%40.3f" % num2

# return a space before positive numbers
print "% 15.3f" % num3
print "% 15f" % num4
print f3 % num2
print f4 % num2
print f5 % num2
print f6 % num2
print f7 % num2
print f8 % num2
print f9 % num2
print f9 % var2
print f9 % var3
print f9 % var4


'''
