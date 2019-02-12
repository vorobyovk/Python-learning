import json

filename = 'player_settings.txt'
myfile = open(filename, mode='w', encoding='Latin-1')

player1 = {
    'PlayerName' : "Donald Trump",
    'Score' : 345,
    'awards' : ["OR", "NV", "NY"]
}

player2 = {
    'PlayerName': "Hillary Clinton",
    'Score': 346,
    'awards': ["WI", "IX", "MI"]
}

myplayers = []

myplayers.append(player1)
myplayers.append(player2)

#---------save by JSON ---------------

json.dump(myplayers, myfile)
myfile.close()

#----------open with JSON------------

myfile = open(filename, mode='r', encoding='Latin-1')
json_data = json.load(myfile)

for player in json_data:
    print("Player name is: " + str(player['PlayerName']))
    print("Player score is :" + str(player['Score']))
    print("Player awards in : " + str(player["awards"]))

