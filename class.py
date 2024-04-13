class Input:
    @staticmethod
    def get_integer(prompt):
        while True:
            try:
                return int(input(prompt))
            except ValueError:
                print("Input harus berupa bilangan bulat.")

    @staticmethod
    def get_float(prompt):
        while True:
            try:
                return float(input(prompt))
            except ValueError:
                print("Input harus berupa bilangan.")

    @staticmethod
    def get_string(prompt):
        return input(prompt)

    @staticmethod
    def get_yes_no(prompt):
        while True:
            response = input(prompt).strip().lower()
            if response in {"y", "yes"}:
                return True
            elif response in {"n", "no"}:
                return False
            else:
                print("Masukkan 'y' atau 'n'.")

# Contoh penggunaan:
if __name__ == "__main__":
    age = Input.get_integer("Masukkan usia Anda: ")
    print("Usia Anda:", age)

    height = Input.get_float("Masukkan tinggi Anda (dalam meter): ")
    print("Tinggi Anda:", height)

    name = Input.get_string("Masukkan nama Anda: ")
    print("Nama Anda:", name)

    likes_pizza = Input.get_yes_no("Apakah Anda suka pizza? (y/n): ")
    if likes_pizza:
        print("Anda suka pizza!")
    else:
        print("Anda tidak suka pizza.")
