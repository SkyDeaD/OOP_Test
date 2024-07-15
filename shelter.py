from animal import Animal, AnimalType, animal_cases
from tabulate import tabulate
from colorama import Fore, Style

class AnimalShelter:
    def __init__(self):
        self.animals = []

    def add_animal(self, name, age, color, animal_type):
        animal = Animal(name, age, color, animal_type)
        self.animals.append(animal)
        print(Fore.GREEN + f'\n{animal_cases[animal_type]["singular"].capitalize()} добавлен(а):' 
              f' Кличка - {name}, Возраст - {age} лет, Цвет - {color}\n' + Style.RESET_ALL)

    def show_animals(self, animal_type):
        print(Fore.BLUE + f'\n{animal_cases[animal_type]["plural"].capitalize()} в приюте:' + Style.RESET_ALL)
        table_data = [
            [animal.name, animal.age, animal.color] 
            for animal in self.animals 
            if animal.animal_type == animal_type
        ]
        if table_data:
            print(tabulate(table_data, headers=["Кличка", "Возраст", "Цвет"], tablefmt="pretty"))
        else:
            print(Fore.YELLOW + "\nНет животных этого типа.\n" + Style.RESET_ALL)
