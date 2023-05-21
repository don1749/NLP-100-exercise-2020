import sys

n = int(sys.argv[1])
with open('popular-names.txt', 'r') as inp, \
    open('Output/firstNLines.txt', 'w') as out:
    out.writelines("".join(inp.readlines()[:n]))