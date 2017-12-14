class Student:
	def __init__(self, name, surname):

		self.name = name
		self.surname = surname
		self.grades = {}
		self.qusPoints = 0
		self.GPA = 0
		self.points = {}
        #these are the instance variables that i have defined to store and access
		
	def getName(self):
		
		return self.name
	#this will return the name of the student
	
	def getSurname(self):
		
		return self.surname
	#this will return the surname of the student
	
	def addGrades(self, gradeStr, credHours):
		
		self.grades[gradeStr] = credHours
		#each grade is assigned to the credit hours
        
	def getGrades(self):
                
		return self.grades
        #this will return the grades 		
	def getHours(self):
        #this will get the hours by copying the grades that have been added by the user and copying it to sum of hours
		sum_hours = 0
		for i in self.grades.values():
			sum_hours = sum_hours + i
		return sum_hours
	
	def getQPoints(self):       
		self.points['A'] = 4.0
		self.points['A-'] = 3.7
		self.points['B+'] = 3.3
		self.points['B'] = 3.0
		self.points['B-'] = 2.7
		self.points['C+'] = 2.3
		self.points['C'] = 2.0
		self.points['C-'] = 1.7
		self.points['D+'] = 1.3
		self.points['D'] = 1.0
		self.quaPoints = 0
	#this will assign each of the string to each value of the grades
		for (k,v) in self.grades.items():
			self.quaPoints = self.quaPoints + (self.points[k]*v)
		return self.quaPoints
	#this for loop will add the quality points to the points which store key and value and add it back to the quality points
	def getGPA(self):	
	#this will get the grade points average
		try:			
			self.GPA = self.getQPoints()/(self.getHours())
		except:
			self.GPA = None
		return self.GPA
	
	def __str__(self):
        
		return self.surname + "," + self.name + ":" + str(self.grades.items()) + ";" + "GPA:" + str(self.getGPA())
#this is the list of the current students that have been made by me, which will be stored into the innit class.
stud1 = Student("Tim", "Blake")
stud2 = Student("Mary", "Watson")

print(stud1.getName())
print(stud2.getSurname())
print(stud1)
#stud1.addGrades("A", 15.0)
#stud1.addGrades("B", 10.0)
stud2.addGrades("B", 15.0)
stud2.addGrades("D+", 10.0)
#stud2.addGrades("C+", 10.0)
print(stud1)
print(stud1.getGrades())
print (stud2)
print(stud2.getGrades())
st1hours = stud1.getHours()
st2Qpts = stud2.getQPoints()
st2Qpts = stud2.getQPoints()
st2hours = stud2.getHours()
print(st2hours)
print(st2hours, st2Qpts)
print(stud2.getGPA())
#print(stud1)
