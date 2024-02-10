import urllib, json, requests

def displayEvents():

    # api-endpoint
    URL = "http://localhost:1337/api/events/?populate=%2A"
    
    # location given here
    #location = "delhi technological university"
    
    # defining a params dict for the parameters to be sent to the API
    #PARAMS = {'address':location}
    
    # sending get request and saving the response as response object
    r = requests.get(url = URL) #, params = PARAMS)
    
    # extracting data in json format
    #below is a dictionary of a list of dictionaries
    data = r.json()

    # below will get you a list of dictionaries, each related to an entry
    ddata = data["data"]
    # event extracts each event, which is a dictionary from the list


    #evets list
    eventsList = []

    for event in ddata:
        # attributes in this dictionary, is another dictionary
        attributes = event["attributes"]
        # now get what you need from the attributes
        title = attributes["title"]
        eventDate = attributes["eventDate"]
        category = attributes["Category"]

        # description and media are a little more complex
        # for the description
        description = attributes["description"]

        # for the media i get a dictionary
        media = attributes["media"]
        #below i will pull the first value from the dictionary which is a list
        temp = media["data"]
        # list only has one entry which is a dictionary so lets get that below
        temp = temp[0]
        # now below we will get the attributes dictionary, which is another dictionary
        temp = temp["attributes"]
        # below get the formats which is another dictionary
        temp = temp["formats"]
        # below choose the size, which will return another dictionary
        temp = temp["small"]
        # below get the url from the dictionary
        media = temp["url"]


        # now we can append it for a proper url from a get request
        media = "http://localhost:1337" + media


        # add each of these attributes to an event list (in order title, media, description, eventDate, category),
        # and add the event list to an events list
        eventList = []
        eventList.append(title)
        eventList.append(media)
        eventList.append(description)
        eventList.append(eventDate)
        eventList.append(category)

        eventsList.append(eventList)



    return eventsList
    
def displayFundRaiserEvents():
    category = "Fund Raiser"
    URL = "http://localhost:1337/api/events?filters[Category][$eq]=" + category + "&populate=%2A"


    # sending get request and saving the response as response object
    r = requests.get(url = URL) #, params = PARAMS)
    
    # extracting data in json format
    #below is a dictionary of a list of dictionaries
    data = r.json()

    # below will get you a list of dictionaries, each related to an entry
    ddata = data["data"]
    # event extracts each event, which is a dictionary from the list


    #evets list
    eventsList = []

    for event in ddata:
        # attributes in this dictionary, is another dictionary
        attributes = event["attributes"]
        # now get what you need from the attributes
        title = attributes["title"]
        eventDate = attributes["eventDate"]
        category = attributes["Category"]

        # description and media are a little more complex
        # for the description
        description = attributes["description"]

        # for the media i get a dictionary
        media = attributes["media"]
        #below i will pull the first value from the dictionary which is a list
        temp = media["data"]
        # list only has one entry which is a dictionary so lets get that below
        temp = temp[0]
        # now below we will get the attributes dictionary, which is another dictionary
        temp = temp["attributes"]
        # below get the formats which is another dictionary
        temp = temp["formats"]
        # below choose the size, which will return another dictionary
        temp = temp["small"]
        # below get the url from the dictionary
        media = temp["url"]


        # now we can append it for a proper url from a get request
        media = "http://localhost:1337" + media


        # add each of these attributes to an event list (in order title, media, description, eventDate, category),
        # and add the event list to an events list
        eventList = []
        eventList.append(title)
        eventList.append(media)
        eventList.append(description)
        eventList.append(eventDate)
        eventList.append(category)

        eventsList.append(eventList)



    return eventsList
