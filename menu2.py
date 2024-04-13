import pyfiglet
from termcolor import colored

def print_menu():
    ascii_banner = pyfiglet.figlet_format("Termux Menu")
    colored_banner = colored(ascii_banner, color='cyan')
    print(colored_banner)
    print(colored("1. Option 1", 'yellow'))
    print(colored("2. Option 2", 'yellow'))
    print(colored("3. Option 3", 'yellow'))
    print(colored("4. Exit ", 'red'))

def main():
    while True:
        print_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            print(pyfiglet.figlet_format("Option 1 Selected", font="block"))
            # Add code for Option 1
        elif choice == '2':
            print(pyfiglet.figlet_format("Option 2 Selected", font="starwars"))
            # Add code for Option 2
        elif choice == '3':
            print(pyfiglet.figlet_format("Option 3 Selected", font="digital"))
            # Add code for Option 3
        elif choice == '4':
            print(pyfiglet.figlet_format("Exiting. Goodbye!", font="slant"))
            break
        else:
            print(colored("Invalid choice. Please enter a valid option.", 'red'))

if __name__ == "__main__":
    main()
