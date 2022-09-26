'''
Write a Python program to read last n lines of a file.
'''

def read_lastline(fname):
    f = open(fname)
    lines = f.readlines()
    lastline = lines[-2:]

    print(type(lastline))
    print(lastline)
    f.close()

if __name__ == "__main__":
    read_lastline("text.txt")