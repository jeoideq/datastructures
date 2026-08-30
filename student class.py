class Student():
    def __init__(self,s,y,n,a):
        self.subject=s

        self.year=y
        self.name=n
        self.age=a

    def display(self):
        print(self.subject,self.year,self.name,self.age)
    
school=Student("math",2,"jade",20)
school.display()

school2=Student("english",1,"sarah",18)
school2.display()


print(school2.year)
#no parameters can be refered to 

class Marks(Student):
    def __init__(self,m,b,e,s,y,n,a):
        super().__init__(s,y,n,a)
        self.math=m
        self.biology=b
        self.english=e
        self.__password="future"
    
    def display(self):
        print(self.math,self.biology,self.english,self.subject,self.year,self.name,self.age,self.__password)

grade=Marks(36, 59, 87, "physics", 1, "hanna", 23)
grade.display()

print(grade.__password)



        
