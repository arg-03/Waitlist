import header
import functions

print("Welcome to Waitlist\n")
print("\nWhat would you like to do: \n 1) Make a Waitlist\n 2) Add a person to your Waitlist\n 3) remove a person from the Waitlist\n 4) View Waitlist\n 5) Turn Waitlist into file\n 6) Exit Program")

while True:
    try:
        choice = int(input("Enter number to do task: "))
        if choice >= 1 and choice <= 6:
            break
        else:
            print("Invalid input, please enter a number between 1 and 6.")

    except ValueError:
        print("Invalid input, please enter a number between 1 and 6.")


