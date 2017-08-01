# -*- coding: utf-8 -*-


import sys,getopt,re
def main(argv):
    inputfile = ''
    outputfile = ''
    try:
        opts, args = getopt.getopt(argv,"hi:o:")
    except getopt.GetoptError:
        print 'usage:util.py -i <inputfile> -o <outputfile>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'util.py -i <inputfile> -o <outputfile>'
            sys.exit()
        elif opt == '-i':
            inputfile = arg
        elif opt == '-o':
            outputfile = arg
        else:
            print 'error'
    convert(inputfile)

def lines(file):
    for line in file:
        yield line
    yield '\n'

def blocks(file):
    block = []
    for line in lines(file):
        if line.strip():
            block.append(line)
        elif block:
            yield ''.join(block).strip()
            block = []

def convert(inputfile):
    text = open(inputfile).readlines()
    print '<html><head><title>...</title><body>.'
    title = True
    for block in blocks(sys.stdin):
        block = re.sub(r'\*(.+?)\*', r'<em>\l</em>', block)
        if title:
            print '<h1>'
            print block
            print '</h1>'
            title = False
        else:
            print '<p>'
            print block
            print '</p>'



if __name__ == '__main__':
    main(sys.argv[1:])
