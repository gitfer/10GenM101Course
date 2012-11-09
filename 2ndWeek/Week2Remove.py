import pymongo
import sys

# establish a connection to the database
connection = pymongo.Connection("mongodb://localhost", safe=True)

# get a handle to the school database
db=connection.students
grades = db.grades


def find():

    print "find, reporting for duty"

    query = {}
    selector = {'student_id': 1, 'score':1, '_id': 1}

    try:
        cursor = grades.find(query, selector).sort([('student_id',pymongo.ASCENDING),('score',pymongo.ASCENDING)])
	
    except:
        print "Unexpected error:", sys.exc_info()[0]

    sanity = 0
    prev_studid = 0
    cur_studid = 0
    prev_id = 0
    for doc in cursor:
	if(cur_studid != doc['student_id']):
		cur_studid = doc['student_id']
		print "rimuovo: "
		print doc['_id']
		grades.remove({'_id': doc['_id']})
        #sanity += 1
        #if (sanity > 10):
            #break
        

find()

