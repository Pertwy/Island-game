import pymongo
from pymongo import MongoClient
from env import *
from excel_in import *
excel_import()

cluster = MongoClient(
    "mongodb+srv://pertwy:Bobbobb0bbob@cluster0.akhrt.mongodb.net/<dbname>?retryWrites=true&w=majority")


def First_Save():
    for x in range(0, 10):
        for y in range(0, 10):
            _id = (x * 10) + y
            collection_env.insert_one({"_id": _id,
                                       "isImpass": eval(find_location_num(x, y)).impass,
                                       "items": eval(find_location_num(x, y)).items,
                                       "Env": eval(find_location_num(x, y)).environment})
    collection_location.insert_one({"_id": 1, "location": location})


def Save():
    for x in range(0, 10):
        for y in range(0, 10):
            _id = (x * 10) + y
            print(_id)
            collection_env.update_one({"_id": _id}, {"$set": {"isImpass": eval(find_location_num(x, y)).impass,
                                                              "items": eval(find_location_num(x, y)).items,
                                                              "Env": eval(find_location_num(x, y)).environment}})
    collection_location.update_one(
        {"_id": 1}, {"$set": {"location": location}})


def Load():
    for x in range(0, 10):
        for y in range(0, 10):
            _id = (x * 10) + y
            results = collection_env.find_one({"_id": _id})
            eval(find_location_num(x, y)).impass = results["isImpass"]
            eval(find_location_num(x, y)).items = results["items"]
            eval(find_location_num(x, y)).environment = results["Env"]
    location_download = collection_location.find_one({"_id": 0})
    location = location_download["location"]


# Load a game or start a new?
game = input("New game or Load game? N/L")

if game == "L":
    for db in cluster.list_databases():
        print(db)
    save = input("What is your save called?")
    db = cluster[save]
    collection_env = db["env"]
    collection_location = db["location"]
    Load()

if game == "N":
    save = input("Name your save")
    db = cluster[save]
    collection_env = db["env"]
    collection_location = db["location"]
    print("Put a long ass intro here so that people read it while the game is loading")
    First_Save()


# Actual Game Loop
win = False
while win == False:
    user_input = input("what do you want to do")
    length = len(user_input.split())

    if user_input == "save" or user_input == "Save":
        Save()

    if user_input == "actions" or user_input == "Actions":
        eval(find_location()).actions_list()

    if user_input == "look" or user_input == "Look":
        eval(find_location()).look()

    if user_input == "inventory" or user_input == "Inventory":
        eval(find_location()).view_inventory()

    if user_input == "dig" or user_input == "Dig":
        eval(find_location()).dig()

    if user_input == "items" or user_input == "Items":
        eval(find_location()).item_list()

    if length >= 2:
        user_input_split = user_input.split(" ")
        user_input_action = user_input_split[0]
        user_input_arg = user_input_split[1]

        if user_input_action == "Move" or user_input_action == "move":
            eval(find_location()).move(user_input_arg)

        elif user_input_action == "Pick":
            user_input_arg = (user_input.replace("Pick", "")).strip()
            eval(find_location()).pick_up(user_input_arg)

        elif user_input_action == "pick":
            user_input_arg = (user_input.replace("pick", "")).strip()
            eval(find_location()).pick_up(user_input_arg)

        elif user_input_action == "Place":
            user_input_arg = user_input.replace("Place", "")
            eval(find_location()).place(user_input_arg)

        elif user_input_action == "place":
            user_input_arg = user_input.replace("place", "")
            eval(find_location()).place(user_input_arg)

        elif user_input_action == "Use" or user_input_action == "use":
            eval(find_location()).use(user_input_arg)

    if length == 3:
        user_input_split = user_input.split(" ")
        user_input_action = user_input_split[0]
        user_input_arg1 = user_input_split[1]
        user_input_arg2 = user_input_split[2]

        if user_input_action == "Combine" or user_input_action == "combine":
            eval(find_location()).combine(user_input_arg1, user_input_arg2)

    # if eval(find_location()).first_time == True:
        # print(eval(find_location()).long_desc)
    # else:
        # print(eval(find_location()).short_desc)

    eval(find_location()).first_time == False


'''
tiles = {}
for x in range(1, 10):
    for y in range(1, 10):
        #("{0}_{1}").format(number_dic[x], number_dic[y]) = Env()
        #tiles["{0}_{1}".format(number_dic[x], number_dic[y])] = Env()
        number_dic[x] + "_" + number_dic[y] = Env()')
'''
