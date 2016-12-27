'''
You are given two classes, Person and Student, where Person is the base class and Student is the derived class. Completed code for Person and a declaration for Student are provided for you in the editor. Observe that Student inherits all the properties of Person.

Complete the Student class by writing the following:

A Student class constructor, which has  parameters:
A string, firstName.
A string, lastName.
An integer, id.
An integer array (or vector) of test scores, scores.
A char calculate() method that calculates a Student object's average and returns the grade character representative of their calculated average:
'''

class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    def __init__(self, firstName, lastName, idNumber, scores):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber
        self.scores = scores


    def calculate(self):

        sum = 0
        for score in self.scores:
            sum += score

        average = sum/(len(self.scores))

        if average >= 90 and average <= 100:
            letterGrade = 'O'
        elif average >= 80 and average < 90:
            letterGrade = 'E'
        elif average >= 70 and average < 80:
            letterGrade = 'A'
        elif average >= 55 and average < 70:
            letterGrade = 'P'
        elif average >= 40 and average < 55:
            letterGrade = 'D'
        elif average < 40:
            letterGrade = 'T'

        return letterGrade


line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())
