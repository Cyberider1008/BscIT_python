#Write a Python program to read an entire text file.


def file_read(file_name):
    txt =open(file_name)
    print(txt.read())

file_read('text.txt')
