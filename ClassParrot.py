class Parrot(object):
    #class attribute
    species = "bird"
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def sing(self,song):
        return "{} sings {}".format(self.name,song)

    def dance(self):
        return "{} is now dancing".format(self.name)

mithu = Parrot("mithu",10)
mithi = Parrot("mithi",15)

#accessing the class attributes
print("mithu is a {}".format(mithu.__class__.species))
print("mithi is a {}".format(mithi.__class__.species))

#accessing instance attributes
print("{} is {} years old".format(mithu.name,mithu.age))
print("{} is {} years old".format(mithi.name,mithi.age))

#calling our instance methods
print(mithu.sing("happy"))
print(mithu.dance())
