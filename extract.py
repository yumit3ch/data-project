import requests
import json

#Python Requests get() Method from w3schools
url = "https://www.freetogame.com/api/games" #api endpoint
response = requests.get(url) #GET request to the API endpoint

if response.status_code == 200: #if the request was successful
    print("Successfully connected to the API", response.status_code, "- ", response.reason)
    
    games_data = response.json() #turn JSON response into python object
    with open('raw_games.json', 'w') as file: #save the raw data to a JSON file
        json.dump(games_data, file, indent=4) #dump data into a JSON file with indentation for readability
        
    print("Raw data successfully saved to 'raw_games.json'!")

    # data = json.loads(response.text) #turn the JSON response into a Python object
    # print(type(data)) #data type of the parsed JSON response
    # print("Number of games retrieved: ", len(data)) #number of games retrieved
    # print("First game retrieved: ", data[0]) #print the first game retrieved

    # for game in data:
    #     print("Game title: ", game["title"]) #print the title of each game

else:
    print("Failed to get data. Status code:", response.status_code, "- ", response.reason)
    