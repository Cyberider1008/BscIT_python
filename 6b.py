#Write a Python program to append text to a file and display the text.

def append_file(fname):
    f = open(fname, '+a')
    f.write("hello beta ji, hahaha")
    f.close()

if __name__ == "__main__":
    append_file("text.txt")