class Player:
    def __init__(self, name, category):
        self.name = name
        self.category = category

    def introduce(self):
        print("Hi I am {}, and I am of {} category".format(self.name, self.category))

class Wizard(Player):
    def __init__(self, name):
        super().__init__(name, category='wizard')

    def play(self):
        print("{} {} starting to play".format(self.category, self.name))

w = Wizard('khalifa')
w.introduce()
w.play()
