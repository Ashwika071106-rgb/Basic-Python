class Dog(object):
    species = "Canis familiaris"
    def __init__(self,name,age,breed):
        self.name = name
        self.age = age
        self.breed = breed

    def bark(self):
        return "{} is barking".format(self.name)

    def eating(self,food):
        return "{} is eating {}".format(self.name,food)

bob = Dog("Bob",5,"Shepherd")
daisy = Dog("Daisy",10,"Bulldog")

print("I am {}. I am a {} and am {} years old".format(bob.name,bob.breed,bob.age))
print("I am {}. I am a {} and am {} years old".format(daisy.name,daisy.breed,daisy.age))

print("Bob and Daisy are {}".format(bob.__class__.species))

print(bob.bark())
print(daisy.bark())

print(bob.eating("bread"))
print(daisy.eating("meat"))