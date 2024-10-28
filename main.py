import header
import functions

print("\nWelcome to Waitlist")
print("\nWhat would you like to do: \n \n 1) Make a Waitlist\n 2) Add a person to your Waitlist\n 3) remove a person from the Waitlist\n 4) View Waitlist\n 5) Turn Waitlist into file\n 6) Exit Program\n")

#Initialize Queue
queue = header.FIFOQueue()
while True:
    try:
        choice = int(input("Enter number to do task: "))
        if choice >= 1 and choice <= 6:
            break
        else:
            print("Invalid input, please enter a number between 1 and 6.")

    except ValueError:
        print("Invalid input, please enter a number between 1 and 6.")

while choice != 6:
    if choice == 1:
        queue.listName = input("Enter name of Waitlist: ")
        print(f'{queue.listName} Waitlist Created')

    elif choice == 2:
        queue.addPerson()
        print("Added Person")
    
    elif choice == 3:
        queue.removePerson()
        print("Removed Person")
    
    elif choice == 4:
        queue.viewList()
        print("Waitlist: ")
        
     
    elif choice == 5:
        queue.save2File()
        print("Waitlist turned into file")

    choice = int(input("Enter number to do task or enter 6 to exit: "))