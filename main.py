import sys
sys.stdout.reconfigure(encoding='utf-8')

from pet import Pet

def main():
    print("🐾 Welcome to the Virtual Pet Simulator 🐾")
    name = input("What would you like to name your pet? ")
    my_pet = Pet(name)

    while True:
        # Display actions menu
        print("\nChoose an action:")
        print("1. Feed your pet")
        print("2. Let your pet sleep")
        print("3. Play with your pet")
        print("4. Train your pet")
        print("5. Show pet status")
        print("6. Show tricks")
        print("7. Quit")

        # Get user choice
        choice = input("Enter your choice: ")

        if choice == "1":
            my_pet.eat()
        elif choice == "2":
            my_pet.sleep()
        elif choice == "3":
            my_pet.play()
        elif choice == "4":
            trick = input("What trick do you want to teach? ")
            my_pet.train(trick)  # Calls the train method from Pet class
        elif choice == "5":
            my_pet.get_status()  # Show current status (hunger, energy, happiness)
        elif choice == "6":
            my_pet.show_tricks()  # Show all tricks the pet has learned
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()




