#Write a Python script to sort (ascending and descending) a dictionary by value

generation = {'1G':1990,'5G':2022, '3G':2004, '4G':2014,  '2G':2000,}

for key,value in sorted(generation.items()):
    print(key, value)

