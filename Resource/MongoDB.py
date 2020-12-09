import sys
from datetime import datetime as DT
import json

from pymongo import MongoClient

from Resource.Resource0 import getList
from Resource.Resource2 import getList2

jsonList = []

# Establish MongoDB access for Login info
# pulls database list information
myList = getList()
# MongoDB Client method settings
R0C = MongoClient("mongodb+srv://" + myList[0] + ":" + myList[1] + "@" + myList[2] +
                  ".mjmit.mongodb.net/" + myList[3] + "?retryWrites=true&w=majority")
# MongoDB name
R0DB = R0C[myList[3]]

# Establish MongoDB access for Weather Data
# pulls database list information
myList2 = getList2()
# MongoDB CLient method Settings
R2C = MongoClient("mongodb+srv://" + myList2[0] + ":" + myList2[1] + "@" + myList2[2] +
                  ".mjmit.mongodb.net/" + myList2[3] + "?retryWrites=true&w=majority")
# MongoDB name
R2DB = R2C[myList2[3]]


def mongoDBBuilderUser(username, password, email):
    now = DT.now().strftime("%Y-%m-%d, %H:%M:%S")

    jsonItem = {"username": username, "password": password, "email": email, "created": now}

    jsonList.append(jsonItem)


def mongoDBUploadUser():
    try:
        R0DB[myList[3]].insert_one(jsonList[0])
    except:
        e = sys.exc_info()[0]
        print(e)


def mongoDBGetCollectionDays():
    myCollections = list(R2DB.list_collection_names())

    return myCollections


def mongoDBGetCollectionData(date):
    location = "web/Jata.json"
    myDocuments = list(R2DB[str(date)].find())

    newList = []
    for doc in myDocuments:
        del doc['_id']
        print("Striping _id from MongoDB Records" + doc)
        newList.append([doc['time'], doc['temperature'], doc['humidity']])

    print("Writing file")
    with open(location, 'w+', encoding='utf-8') as output:
        json.dump(newList, output)

