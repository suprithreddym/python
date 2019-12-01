import shelve
locations = shelve.open("locations")
locations['0'] = {"desc": "you are sitting in front of computer learning python",
                  "exits": {},
                  "namedexits": {}}
locations['1'] = {"desc":"you are sitting at the end of the road before a small brick building",
                  "exits": {"W": '2', "E": '3', "N": '5', "S": '4', "Q": '0'},
                  "namedexits": {"2": '2', "3": '3', "5": '5', "4": '4'}}

locations['2'] = {"desc":"you are at the top of the hill",
                  "exits":{"N": '5', "Q": '0'},
                  "namedexits":{"5": '5'}}

locations['3'] = {"desc": "you are inside a building",
                  "exits": {"W": '1', "Q": '0'},
                  "namedexits": {"1":'1'}}

locations['4'] = {"desc":"you are in the valley behind a stream",
                  "exits":{"N": '1', "W": '2', "Q": '0'},
                  "namedexits": {"1": '1', "2": '2'}}
locations['5'] = {"desc":"you are in the forest",
                  "exits":{"W": '2', "S": '1', "Q": '0'},
                  "namedexits": {"2": '2', "1": '1'}}

locations.close()

vocabulary = shelve.open("vocabulary")
vocabulary["QUIT"]= "Q"
vocabulary["NORTH"] = "N"
vocabulary["SOUTH"] = "S"
vocabulary["EAST"] = "E"
vocabulary["WEST"] = "W"
vocabulary["ROAD"] = "1"
vocabulary["HILL"] = "2"
vocabulary["Building"] = "3"
vocabulary["VALLEY"] = "4"
vocabulary["FOREST"] = "5"

vocabulary.close()