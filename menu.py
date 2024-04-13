import os
import subprocess
import time
import sys
import pyfiglet
def show_menu():
    ascii_banner = pyfiglet.figlet_format("Termux Menu")
    print(ascii_banner)
    print("1. update")
    print("4. Keluar")
def update_upgrade_termux():
    try:
        # Update package lists
        subprocess.check_call(['pkg', 'update'])

        # Upgrade installed packages
        subprocess.check_call(['pkg', 'upgrade', '-y'])

        print("Update dan upgrade selesai.")

    except subprocess.CalledProcessError as e:
        print("Terjadi kesalahan saat melakukan update dan upgrade:", e)
 
def main():
    while True:
        show_menu()
        choice = input("Pilih menu nomer: ")
        
        if choice == '1':
            print("Anda memilih Option 1")
            # Lakukan no 1
            update_upgrade_termux()
            time.sleep(5)
            os.system('clear')
            
            
            
        elif choice == '2':
            print("Anda memilih Option 2")
            # Lakukan sesuatu untuk Option 2
        elif choice == '3':
            print("Anda memilih Option 3")
            # Lakukan sesuatu untuk Option 3
        elif choice == '4':
            print("Terima kasih!")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih menu yang sesuai.")

if __name__ == "__main__":
    main()
    
