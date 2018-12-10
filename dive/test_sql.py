from toolbox import exit


oldprefix = 'modoer_'
newprefix = 'tbl'


def getTable(line):
    return {'table': line.replace(oldprefix, '').strip()}


def translateAll():
    tempalte = "RENAME TABLE  `tianhelucrd`.`modoer_%(table)s` TO \
`tianhelucrd`.`tbl_%(table)s`;"
    return [tempalte % getTable(line) for line in open("tables.log")]

queries = translateAll()

print("\n".join(queries))

exit()
# end of file
