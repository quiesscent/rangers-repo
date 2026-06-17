

name = "Ronald owere"
age = 27

print(f"Hello {name}, you are a major.")

while True:
    print("\n--- Menu ---")
    print("1. Say Hello")
    print("2. Show your age")
    print("3. Exit")
    
    choice = input("Choose an option: ")
    
    if choice == "1":
        print(f"Hello, {name}!")
    elif choice == "2":
        print(f"You are {age} years old.")
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")
