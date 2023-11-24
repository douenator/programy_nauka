class Animal: #klasa bazowa (rodzic)
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Dog(Animal):
    def voice(self):
        print("Woof!")

class Wolf(Dog):
    def getVoice(self):
        print("Jestem wilkiem,")
        super().voice()

class Cat(Animal):
    def getVoice(self):
        print("Meow!")

dog = Dog("Pierdek", 4)
print(dog.name)
print(dog.age)
dog.voice()

cat = Cat("Puszek", 3)
print(cat.name)
print(cat.age)
cat.getVoice()

wolf = Wolf("Wilczur", 7)
print(wolf.name)
print(wolf.age)
wolf.getVoice()