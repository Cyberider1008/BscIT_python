#Design a class that store the information of student and display the same

class Students:
    def __init__(self, name, sex, course, result):
        self.name = name
        self.sex = sex
        self.course = course
        self.result = result

    def display(self):
        

        print("Name: ", self.name)
        print("Sex : ", self.sex)
        print("course: ", self.course)
        print("result: ", self.result)


s = Students("ashish","M","Bsc IT","90.99")

s.display()
