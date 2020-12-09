import eel

from Resource.MongoDB import mongoDBBuilderUser, mongoDBUploadUser, mongoDBGetCollectionDays, mongoDBGetCollectionData

# web file folder
eel.init('web')


@eel.expose
def registerButtonHandler_py(username, password, email):
    # builds mongoDB user object
    mongoDBBuilderUser(username, password, email)

    # validate unique username and uploads
    mongoDBUploadUser()


@eel.expose
def collectionFetcher_py():

    # fetches the dates of data that are stored in MongoDB collections
    dateList = mongoDBGetCollectionDays()

    for date in dateList:
        eel.availableDatesListAppend_js(date)


@eel.expose
def fetchCollectionData_py(date):

    # This method can get a little cumbersome depending on data python console message inserted to show progressing activity
    print("Fetching Data " + str(date))
    # fetches the data of the date selected by the user in HTML from MongoDB
    mongoDBGetCollectionData(date)
    print("Sending it back to JS")
    eel.dataReadyToViewCanvasJS_js()


eel.start('index.html')
