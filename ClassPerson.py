class Person(object):
    species = "Homo Sapien"
    def __init__(self,name,gender,age,height):
        self.name = name
        self.age = age
        self.gender = gender
        self.height = height

    def speak(self):
        print("Hi! My name is {}".format(self.name))

    def work(self,work):
        return "{} is {}".format(self.name,work)

ashwika = Person("Ashwika","Female",14,5.2)

print(ashwika.speak())
print("I am a {} year old {}".format(ashwika.age,ashwika.gender))
print("I am a {}".format(ashwika.__class__.species))
print(ashwika.work("studying"))