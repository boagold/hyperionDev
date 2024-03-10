def get_user_input():
    while True:
        try:
            user_input = input("Please enter some data: ").strip()  # Remove leading/trailing whitespace
            if not user_input:
                raise ValueError("Input cannot be empty. Please try again.")
            return user_input
        except KeyboardInterrupt:
            # Handle Ctrl+C to gracefully exit the program
            print("\nProgram terminated.")
            exit()
        except ValueError as ve:
            print(ve)  # Print specific error message
        except Exception as e:
            print("An unexpected error occurred:", e)


def main():
    user_input = get_user_input()
    print("You entered:", user_input)


if __name__ == "__main__":
    main()
