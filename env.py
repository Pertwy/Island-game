class Env:

    def __init__(self, x, y, description):
        self.x = x
        self.y = y
        self.description = description

    def actions(self):
        pass


class Sea(Env):
    pass


class Jung(Env):
    pass


class Sand(Env):
    pass


one_one_one = Sea(1, 1, "Furthest corners of the map")
print(one_one_one.description)
