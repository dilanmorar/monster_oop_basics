skills = ['shape shift', 'quiet', 'strong', 'smart', 'smelly']

class Monster():
    def __init__(self, name, colour, skills):
        self.name = name
        self.colour = colour
        self.skills = skills
    def sleep(self):
        return 'zzz'
    def eat(self):
        return 'nom nom nom'
    def scare_attack(self):
        return 'Boo'