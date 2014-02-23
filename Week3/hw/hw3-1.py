import pymongo
import sys
import exceptions
import string

# establish a connection to the database
connection = pymongo.Connection("mongodb://localhost", safe=True)
db=connection.school
students=db.students

def find_lowest_hw(scores):
    lowest = None
    lowest_score = 101

    for item in scores:
        #{u'score': 1.463179736705023, u'type': u'exam'}
        #{u'score': 6.676176060654615, u'type': u'homework'}
        if ((item['type'] == "homework") and (item['score'] < lowest_score)):
            lowest = item
            lowest_score = lowest['score']

    return lowest

def remove_lowest():

    cursor = students.find()

    for student in cursor:
        scores = student['scores']
        lowest = find_lowest_hw(scores)
        if (lowest is not None):
            scores.remove(lowest)

            try:
                students.update({'_id': student['_id']}, {'$set':{'scores':scores}})
            except:
                print "Unexpected Error:", sys.exec_info()[0]
                raise
        else:
            print "Could not find a homework score to process."

remove_lowest()