class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print(f"{self.name}: generic animal sound")

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def sound(self):
        print(f"{self.name}: Woof!")

# Тестовая программа
if __name__ == "__main__":
    # Создаем объект базового класса
    animal = Animal("Generic Animal")
    animal.sound()

    # Создаем объект производного класса
    dog = Dog("Buddy")
    dog.sound()
