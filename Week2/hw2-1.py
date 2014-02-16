import pymongo
import sys

# establish a connection to the database
connection = pymongo.Connection("mongodb://localhost", safe=True)
db=connection.students
grades=db.grades

def find():

    query = {'type':'exam', 'score':{'$gte':65}}
    selector = {'_id':0, 'student_id':1, 'score':1}

    try:
        cursor = grades.find(query,selector).sort('score', pymongo.ASCENDING)

    except:
        print "Unexpected error:", sys.exc_info()[0]

    sanity = 0
    for doc in cursor:
        print doc
        sanity += 1
        if (sanity > 10):
            break

find()
