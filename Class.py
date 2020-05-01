#class is the collection of data member and member functions
#Example- sudent Count is DM & printStudentData is Member funcion
# __init__ is specail member function of class that aslo know as constructor
# taht is being know or called as class name
# OBJECTS of the class are - s,var,var1
class student:
    studentCount=0
    def __init__(self,name,id):
        self.name=name
        self.id=id
        student.studentCount +=1
    def printStudentData(self):
        print("name=",self.name,"id=",self.id)
s = student("Harsh",23)
s.printStudentData()
var=student("rishab",3)
var1=student("Tanshiq",2)
print("Total number of student",student.studentCount)
s.printStudentData()
var.printStudentData()
var1.printStudentData()

#object has right to access DM and MF
print("student.__doc_=",student.__doc__)
print("student.__name__",student.__name__)
print("student.__module__",student.__module__)
print("student.__bases__",student.__bases__)
print("student.__dict__",student.__dict__)


