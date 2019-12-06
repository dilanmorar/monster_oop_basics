from Monster_class import *

monster1 = Monster('Mike', 'green', 'big.')

print(monster1.name)
print(monster1.colour)
print(monster1.skills)

print(monster1.eat())
print(monster1.sleep())
print(monster1.scare_attack())

monster1. add_skills('invisible')
print(monster1.skills)