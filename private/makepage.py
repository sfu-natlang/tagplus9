import sys
if __name__ == '__main__':
    if (len(sys.argv) == 1):
        exit(1)
    else:
        headerf = open('header.txt', 'r')
        headertxt = headerf.read()
        footerf = open('footer.txt', 'r')
        footertxt = footerf.read()
        f = open(sys.argv[1], 'r')
        txt = f.read()
        print headertxt
        print txt
        print footertxt

