class Monster():
    def __init__(self, name = 'jim', colour = 'red', skills = []):
        self.name = name
        self.colour = colour
        self.skills = skills

    def sleep(self):
        return 'zzz'
    def eat(self):
        return 'nom nom nom'
    def scare_attack(self):
        return 'Boo'

    def add_skills(self, skill):
        chosen_monster = self
        chosen_monster.skills.append(skill)
