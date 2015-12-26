# -*- coding: utf-8 -*-

class Cat(object):

    legs_number = 4

    def __init__(self, cat_name):
        self.name = cat_name
        self.is_moving = False

    def run(self):
        self.is_moving = True
        print "I'm running."

    def stop(self):
        self.is_moving = False
        print "I stopped."

    def play(self, toy):
        print "I'm playing with {}.".format(toy)

    def eat(self, *food):
        print food
        joined_food = ", ".join(food)
        print joined_food
        print "I'm eating {}.".format(joined_food)


cat = Cat("Murzik")
print cat.legs_number
print cat.name
print Cat.legs_number
cat.run()
print cat.is_moving
cat.stop()
print cat.is_moving
cat.play("ball")
cat.eat("spaghetti")
cat.eat("milk", "sausage")
