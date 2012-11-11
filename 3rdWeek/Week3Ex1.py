import pymongo
import sys

# establish a connection to the database
connection = pymongo.Connection("mongodb://localhost", safe=True)

# get a handle to the school database
db=connection.school
students = db.students


def find():

    print "find, reporting for duty"

    query = {}
    selector = { 'scores.score': 1, 'scores.type': 1, '_id':1}

    try:
        cursor = students.find(query, selector)
	
    except:
        print "Unexpected error:", sys.exc_info()[0]

    sanity = 0
    for doc in cursor:
		punt = doc['scores']
		minimoAttuale = minore(doc)
		#print doc
		students.update( { "_id" : doc['_id'] }, { "$pull" : { "scores" : {"score" : minimoAttuale } } } );
		print minimoAttuale

		print doc
        
def minore(obj):
	if 'scores' in obj:
		elems = []
		for n in obj['scores']:
			if n['type'] == 'homework':
				elems.append(n['score'])
				print n
				#print elems
		#print min(elems)
		return min(elems)
			#if n['score'] < minore:
				#minore=n['score']
				#print n['score']<minore
				#print minore 

find()

