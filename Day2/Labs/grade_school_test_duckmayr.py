class School(object):
	def __init__(self, name):
		self.name = name
		self.roster = {1: [], 2: [], 3: [], 4: [], 5: [], 6: []}
		
	def addStudent(self, name, grade):
		self.roster[grade].append(name)
		print "Added %s to the %s grade roster." % (name, grade)
		
	def printRoster(self, grade):
		print "In grade %s, we have the following students: \n %s" %(grade, '\n'.join(self.roster[grade]))
		#print '\n'.join(self.roster[grade])
	
	def __str__(self):
		output = ''
		for grades in self.roster.keys():
			output += "Grade %d: %s \n" % (grades, str(' '.join(sorted(self.roster[grades]))))
		return output
		
	def __repr__(self):
		return self.__str__()











"""
import unittest

from school import School


class SchoolTest(unittest.TestCase):
    def setUp(self):
        self.school = School("Haleakala Hippy School")

    def test_an_empty_school(self):
        self.assertEqual({}, self.school.db)

    def test_add_student(self):
        self.school.add("Aimee", 2)
        self.assertEqual({2: {"Aimee"}}, self.school.db)

    def test_add_more_students_in_same_class(self):
        self.school.add("James", 2)
        self.school.add("Blair", 2)
        self.school.add("Paul", 2)
        self.assertEqual({2: {"James", "Blair", "Paul"}}, self.school.db)

    def test_add_students_to_different_grades(self):
        self.school.add("Chelsea", 3)
        self.school.add("Logan", 7)
        self.assertEqual({3: {"Chelsea"}, 7: {"Logan"}}, self.school.db)

    def test_get_students_in_a_grade(self):
        self.school.add("Franklin", 5)
        self.school.add("Bradley", 5)
        self.school.add("Jeff", 1)
        self.assertEqual({"Franklin", "Bradley"}, self.school.grade(5))

    def test_get_students_in_a_non_existant_grade(self):
        self.assertEqual(None, self.school.grade(1))

    def test_sort_school(self):
        self.school.add("Jennifer", 4)
        self.school.add("Kareem", 6)
        self.school.add("Christopher", 4)
        self.school.add("Kyle", 3)
        sorted_students = {
            3: ("Kyle",),
            4: ("Christopher", "Jennifer",),
            6: ("Kareem",)
        }
        self.assertEqual(sorted_students, self.school.sort())

if __name__ == '__main__':
    unittest.main()
"""