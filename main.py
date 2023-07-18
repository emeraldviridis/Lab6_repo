def encode(password):
    return "".join(chr(ord(char) + 3) for char in password)


def decode(password):
    return "".join(chr(ord(char) - 3) for char in password)


def main():
    stored_password = None
    while True:
        print("Menu\n-------------")
        print("1. Encode\n2. Decode\n3. Quit")
        option = input("Please enter an option: ")

        if option == "1":
            password = input("Please enter your password to encode: ")
            stored_password = encode(password)
            print("Your password has been encoded and stored!")

        elif option == "2":
            if stored_password:
                print(
                    f"The encoded password is {stored_password}, and the original password is {decode(stored_password)}.")
            else:
                print("No encoded password is stored yet.")

        elif option == "3":
            break

        else:
            print("Invalid option. Please enter 1, 2 or 3.")


if __name__ == "__main__":
    main()
