courses = { "Math":["Algebra","Geometry", "Statistic", "Trig"],"Co Sci" :["Python", "Java", "C++"]      }

class Department:
	def __init__(self , dept):
		self.Dept = dept

class Courses(Department):
	def __init__(self, dept, cname, profname):
		super().__init__(dept)

class Person:
	def __init__(self, name, age, address, gender):
		self.name = name
		self.age = age
		self.address = address
		self.gender  = gender

class student(Person)  :
	def __init__( self, name, age, address, gender ):
		self.id = self.getId()
		super().__init__(name,age,address,gender)
#		Person.name= name
#		Person.age= age
#		Person.address= address
#		Person.gender= gender
		 
	
	def getId(self):
		return 0
		
	def toString(self):
		stri = self.name + self.address
		return stri
		


def getClass(mclass):
		if mclass in courses:
			for cclass  in courses[mclass]:
					print(cclass)
          


#getClass("Math")
s1 = student("james", 22, "123 fake st.", "Male")
print (s1.toString())
