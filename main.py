from shelter import AnimalShelter
from menu import display_menu, get_actions
from animal import AnimalType
from colorama import init, Fore, Style

def main():
    init(autoreset=True)
    shelter = AnimalShelter()
    actions = get_actions(shelter)

    while True:
        display_menu()
        choice = input(Fore.CYAN + "Введите номер действия: " + Style.RESET_ALL)
        action = actions.get(choice)
        if action:
            if choice in ["1", "2"]:
                animal_type = {
                    "1": AnimalType.DOG,
                    "2": AnimalType.CAT
                }[choice]
                action(shelter, animal_type)
            else:
                action(shelter)
        else:
            print(Fore.RED + "\nНеверный ввод, попробуйте снова.\n" + Style.RESET_ALL)

if __name__ == "__main__":
    main()
