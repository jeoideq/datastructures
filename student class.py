class Student():
    def __init__(self,s,g,y,n,a):
        self.subject=s
        self.grade=g
        self.year=y
        self.name=n
        self.age=a

    def display(self):
        print(self.subject,self.grade,self.year,self.name,self.age)
    
school=Student("math","C",2,"jade",20)
school.display()

school2=Student("english","A",1,"sarah",18)
school2.display()

print(school.grade)
print(school2.year)
#no parameters can be refered to 
