'''Write a Python script to concatenate following dictionaries to create a new
one.'''

dic1={1:10,2:20}
dic2={3:30,4:40}
dic3={5:50,6:60}


dic1.update(dic2)
print("after update dic2", dic1)

dic1.update(dic3)
print("after update dic3", dic1)