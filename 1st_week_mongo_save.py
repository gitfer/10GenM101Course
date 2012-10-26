import pymongo
import sys

connection = pymongo.Connection("mongodb://localhost", safe=True)

db = connection.test
people = db.people

person = {'name': 'Barack Obama', 'role': 'president'}
try:
	people.insert(person)
except:
	print "ins failed: ", sys.exc_info()[0]

print person

try:
	people.insert(person)
except:
	print "ins failed: ", sys.exc_info()[0]

print person
