from shelter import AnimalShelter
from animal import AnimalType, animal_cases
from colorama import Fore, Style

def add_animal(shelter, animal_type):
    print(Fore.CYAN + f"\nДобавление {animal_cases[animal_type]['genitive']}:" + Style.RESET_ALL)
    animal_name = input(Fore.CYAN + f"Введите кличку {animal_cases[animal_type]['genitive']}: " + Style.RESET_ALL)
    animal_age = input(Fore.CYAN + f"Введите возраст {animal_cases[animal_type]['genitive']}: " + Style.RESET_ALL)
    animal_color = input(Fore.CYAN + f"Введите цвет {animal_cases[animal_type]['genitive']}: " + Style.RESET_ALL)
    shelter.add_animal(animal_name, animal_age, animal_color, animal_type)

def show_dogs(shelter):
    shelter.show_animals(AnimalType.DOG)

def show_cats(shelter):
    shelter.show_animals(AnimalType.CAT)

def exit_program():
    print(Fore.RED + "\nВыход из программы.\n" + Style.RESET_ALL)
    exit()

def display_menu():
    print(Fore.MAGENTA + "\nВыберите действие:" + Style.RESET_ALL)
    print(Fore.CYAN + "1. Добавить собаку" + Style.RESET_ALL)
    print(Fore.CYAN + "2. Добавить кошку" + Style.RESET_ALL)
    print(Fore.CYAN + "3. Показать всех собак" + Style.RESET_ALL)
    print(Fore.CYAN + "4. Показать всех кошек" + Style.RESET_ALL)
    print(Fore.CYAN + "5. Выйти\n" + Style.RESET_ALL)

def get_actions(shelter):
    return {
        "1": add_animal,
        "2": add_animal,
        "3": show_dogs,
        "4": show_cats,
        "5": exit_program
    }
