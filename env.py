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


location = [0, 0]


def find_location():
    return ("{0}_{1}".format(number_dic[location[0]], number_dic[location[1]]))


class Env:

    # The long description will be shown the first time a player enters a square. And if a player uses the look comand
    def add_long_desc(self, long_desc):
        self.long_desc = long_desc

    # The short description will be shown anytime a square is entered which isnt the first
    def add_short_desc(self, short_desc):
        self.short_desc = short_desc

    def is_impass(self, impass):
        self.impass = impass

    def __init__(self):
        self.first_time = True  # first time you enter an area

    def actions_list(self):  # what actions are available?
        print("Print List of actions")

    def look(self):
        print(self.add_long_desc)

    def inventory(self):
        pass

    def dig(self):
        pass

    def pick_up(self, item):
        pass

    def place(self, item):
        pass

    def use(self, item):
        pass

    def combine(self, item1, item2):
        pass

    def move(self, direction):
        if direction == "N" or direction == "n":
            if location[1] == 0:
                print("can't go that was mate")
            elif self.impass == True:
                print("impass mate, bit stuck ent ya")
            else:
                location[1] = location[1] - 1
                self.look()

        elif direction == "S" or direction == "s":
            if location[1] == 10:
                print("can't go that was mate")
            elif self.impass == True:
                print("impass mate, bit stuck ent ya")
            else:
                location[1] = location[1] + 1
                self.look()

        elif direction == "E" or direction == "e":
            if location[0] == 10:
                print("can't go that was mate")
            elif self.impass == True:
                print("impass mate, bit stuck ent ya")
            else:
                location[1] = location[1] + 1
                self.look()

        elif direction == "W" or direction == "w":
            if location[0] == 0:
                print("can't go that was mate")
            elif self.impass == True:
                print("impass mate, bit stuck ent ya")
            else:
                location[1] = location[1] - 1
                self.look()

        else:
            pass  # check again


class Sea(Env):
    pass


class Jung(Env):
    pass


class Sand(Env):
    pass


zero_zero = Env()
zero_one = Env()
zero_one = Env()
zero_one = Env()
zero_one = Env()
zero_one = Env()
zero_one = Env()
zero_one = Env()
zero_one = Env()
zero_one = Env()
zero_one = Env()

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

one_one.is_impass(True)

# print(tiles)
# create all of the env squares

# location is set to start
# what do you want to do?
#
win = False

while win == False:
    user_input = input("what do you want to do")
    length = len(user_input.split())
    eval(find_location()).add_long_desc("Hello")
    eval(find_location()).look()

    if length == 1:
        if user_input == "actions" or "Actions":
            one_one.actions_list()
        elif user_input == "look" or "Look":
            one_one.look()
        elif user_input == "inventory" or user_input == "Inventory":
            one_one.inventory()
        elif user_input == "dig" or user_input == "Dig":
            one_one.dig()

    if length == 2:
        user_input_split = user_input.split(" ")
        user_input_action = user_input_split[0]
        user_input_arg = user_input_split[1]

        if user_input_action == "Move" or user_input_action == "move":
            one_one.move(user_input_arg)
        elif user_input_action == "Pick" or user_input_action == "pick":
            one_one.pick_up(user_input_arg)
        elif user_input_action == "Place" or user_input_action == "place":
            one_one.place(user_input_arg)
        elif user_input_action == "Use" or user_input_action == "use":
            one_one.use(user_input_arg)

    if length == 3:
        user_input_split = user_input.split(" ")
        user_input_action = user_input_split[0]
        user_input_arg1 = user_input_split[1]
        user_input_arg2 = user_input_split[2]

        if user_input_action == "Combine" or user_input_action == "combine":
            one_one.combine(user_input_arg1, user_input_arg2)


'''
tiles = {}
for x in range(1, 10):
    for y in range(1, 10):
        #("{0}_{1}").format(number_dic[x], number_dic[y]) = Env()
        #tiles["{0}_{1}".format(number_dic[x], number_dic[y])] = Env()
        number_dic[x] + "_" + number_dic[y] = Env()')
'''
