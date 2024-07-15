from enum import Enum

class AnimalType(Enum):
    DOG = "dog"
    CAT = "cat"

animal_cases = {
    AnimalType.DOG: {
        "singular": "собака",
        "plural": "собаки",
        "genitive": "собаки"
    },
    AnimalType.CAT: {
        "singular": "кошка",
        "plural": "кошки",
        "genitive": "кошки"
    }
}

class Animal:
    def __init__(self, name, age, color, animal_type):
        self.name = name
        self.age = age
        self.color = color
        self.animal_type = animal_type

    def description(self):
        return f'Кличка - {self.name} \nВозраст - {self.age} \nЦвет - {self.color} \nТип - {animal_cases[self.animal_type]["singular"]}'
