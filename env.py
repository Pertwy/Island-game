number_dic = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
}

action_dic = """look: Look around
move: Move north (N), south (S), East (E), or West (W)
inventory: View your inventory
items: View the items on the floor
dig: Dig 
pick: Pick up an object and put it in your inventory
place: Place an object from your inventory on the floor
use: Use an item
combine: Combine two items
inspect: Inspect an item on the floor or in your inventory"""


# Starting location
location = [0, 0]
inventory = ["inventory"]
answer = ""


def find_location():
    return ("{0}_{1}".format(number_dic[location[0]], number_dic[location[1]]))

def find_location_num(x,y):
    return ("{0}_{1}".format(number_dic[x], number_dic[y]))

def find_location_N():
    return ("{0}_{1}".format(number_dic[location[0]], number_dic[location[1] - 1]))


def find_location_S():
    return ("{0}_{1}".format(number_dic[location[0]], number_dic[location[1] + 1]))


def find_location_E():
    return ("{0}_{1}".format(number_dic[location[0] - 1], number_dic[location[1]]))


def find_location_W():
    return ("{0}_{1}".format(number_dic[location[0] + 1], number_dic[location[1]]))


class Env:

    def __init__(self):
        self.first_time = True  # first time you enter an area
        self.items = []

    # The long description will be shown the first time a player enters a square. And if a player uses the look comand
    def add_long_desc(self, long_desc):
        self.long_desc = long_desc

    # The short description will be shown anytime a square is entered which isnt the first
    def add_short_desc(self, short_desc):
        self.short_desc = short_desc

    def add_environment(self, environment):
        self.environment = environment

    def add_is_impass(self, impass):
        self.impass = impass

    def add_items(self, items):
        self.items.append(items)

    def actions_list(self):  # what actions are available?
        print(action_dic)

    def look(self):
        print(self.long_desc)

    def view_inventory(self):
        print(inventory)

    def item_list(self):
        print("All items on the floor:" + self.items)

    def dig(self):
        pass

    def pick_up(self, item):
        if item in self.items:
            inventory.append(item)
            self.items.remove(item)
        else:
            print("that item is not there")

    def place(self, item):
        if item in inventory:
            inventory.remove(item)
            self.items.append(item)
        else:
            print("You do not have that item")

    def use(self, item):
        pass

    def combine(self, item1, item2):
        pass

    def move(self, direction):
        if direction == "N" or direction == "n":
            if location[1] == 0:
                print("can't go that was mate")
            elif eval(find_location_N()).environment == "rocks":
                print("The rocks are too treterous, you can not pass")
            elif eval(find_location_N()).environment == "denseForest" and "machette" not in inventory:
                print(
                    "The forest is too dense to walk through but looks like it could be cut down")
            elif eval(find_location_N()).environment == "denseForest" and "machette" in inventory:
                answer = input("cut down dense forest with machette? Y/N")
                if answer == "Y":
                    location[1] = location[1] - 1
                    eval(find_location()).environment = "forest"
                    print("You cut down that forest and move forward")
                elif answer == "N":
                    print("You can cut down that forest, but maybe later")
            else:
                location[1] = location[1] - 1

        elif direction == "S" or direction == "s":
            if location[1] == 10:
                print("can't go that was mate")
            # elif self.impass == True:
                #print("impass mate, bit stuck ent ya")
            else:
                location[1] = location[1] + 1

        elif direction == "E" or direction == "e":
            if location[0] == 10:
                print("can't go that was mate")
            # elif self.impass == True:
                #print("impass mate, bit stuck ent ya")
            else:
                location[0] = location[0] + 1

        elif direction == "W" or direction == "w":
            if location[0] == 0:
                print("can't go that was mate")
            # elif self.impass == True:
                #print("impass mate, bit stuck ent ya")
            else:
                location[0] = location[0] - 1

        else:
            pass  # check again
        print(location)


zero_zero = Env()
one_zero = Env()
two_zero = Env()
three_zero = Env()
four_zero = Env()
five_zero = Env()
six_zero = Env()
seven_zero = Env()
eight_zero = Env()
nine_zero = Env()
ten_zero = Env()

zero_one = Env()
one_one = Env()
two_one = Env()
three_one = Env()
four_one = Env()
five_one = Env()
six_one = Env()
seven_one = Env()
eight_one = Env()
nine_one = Env()
ten_one = Env()

zero_two = Env()
one_two = Env()
two_two = Env()
three_two = Env()
four_two = Env()
five_two = Env()
six_two = Env()
seven_two = Env()
eight_two = Env()
nine_two = Env()
ten_two = Env()

zero_three = Env()
one_three = Env()
two_three = Env()
three_three = Env()
four_three = Env()
five_three = Env()
six_three = Env()
seven_three = Env()
eight_three = Env()
nine_three = Env()
ten_three = Env()

zero_four = Env()
one_four = Env()
two_four = Env()
three_four = Env()
four_four = Env()
five_four = Env()
six_four = Env()
seven_four = Env()
eight_four = Env()
nine_four = Env()
ten_four = Env()

zero_five = Env()
one_five = Env()
two_five = Env()
three_five = Env()
four_five = Env()
five_five = Env()
six_five = Env()
seven_five = Env()
eight_five = Env()
nine_five = Env()
ten_five = Env()

zero_six = Env()
one_six = Env()
two_six = Env()
three_six = Env()
four_six = Env()
five_six = Env()
six_six = Env()
seven_six = Env()
eight_six = Env()
nine_six = Env()
ten_six = Env()

zero_seven = Env()
one_seven = Env()
two_seven = Env()
three_seven = Env()
four_seven = Env()
five_seven = Env()
six_seven = Env()
seven_seven = Env()
eight_seven = Env()
nine_seven = Env()
ten_seven = Env()

zero_eight = Env()
one_eight = Env()
two_eight = Env()
three_eight = Env()
four_eight = Env()
five_eight = Env()
six_eight = Env()
seven_eight = Env()
eight_eight = Env()
nine_eight = Env()
ten_eight = Env()

zero_nine = Env()
one_nine = Env()
two_nine = Env()
three_nine = Env()
four_nine = Env()
five_nine = Env()
six_nine = Env()
seven_nine = Env()
eight_nine = Env()
nine_nine = Env()
ten_nine = Env()

zero_ten = Env()
one_ten = Env()
two_ten = Env()
three_ten = Env()
four_ten = Env()
five_ten = Env()
six_ten = Env()
seven_ten = Env()
eight_ten = Env()
nine_ten = Env()
ten_ten = Env()
