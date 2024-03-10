def get_user_input():
    while True:
        try:
            user_input = input("Please enter some data: ")
            # Check if the input is not empty
            if user_input.strip():
                return user_input
            else:
                print("Input cannot be empty. Please try again.")
        except KeyboardInterrupt:
            # Handle Ctrl+C to gracefully exit the program
            print("\nProgram terminated.")
            exit()
        except Exception as e:
            print("An error occurred:", e)


def main():
    user_input = get_user_input()
    print("You entered:", user_input)


if __name__ == "__main__":
    main()
