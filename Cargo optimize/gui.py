import sys

from main import linkedlist 

def main_menu():
    ll = linkedlist()
    while True:
        print("\n--- Package Manager v0.6 ---")
        print("1. Add Package")
        print("2. Display All Packages")
        print("3. Display Sorted Packages by Distance")
        print("4. Generate Invoice")
        print("5. Exit")
        
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == 1:
            add_package_gui(ll)
        elif choice == 2:
            ll.display()
        elif choice == 3:
            display_sorted_packages(ll)
        elif choice == 4:
            generate_invoice(ll)
        elif choice == 5:
            print("Exiting...")
            sys.exit()
        else:
            print("Invalid choice. Please select from the menu.")

def add_package_gui(ll):
    try:
        weight = float(input("Enter package weight (kg): "))
        length = float(input("Enter package length (m): "))
        width = float(input("Enter package width (m): "))
        height = float(input("Enter package height (m): "))
        value = float(input("Enter package value (VNĐ): "))
        
        print("\nAvailable Destinations:")
        for city in ll.city_distances.keys():
            print(f"- {city}")
        destination = input("Enter destination: ")

        if destination not in ll.city_distances:
            print("Invalid destination. Please choose from the available options.")
            return

        ll.add_package(weight, length, width, height, value, destination)
        print("Package added successfully!")
    except ValueError as ve:
        print(f"Error: {ve}")
    except TypeError as te:
        print(f"Error: {te}")

def display_sorted_packages(ll):
    print("\n--- Sorted Packages by Distance ---")
    ll.sort()  # Sort the linked list by distance
    ll.display()  # Display the sorted list

def generate_invoice(ll):
    try:
        weight_rate = float(input("Enter weight rate (VNĐ per kg): "))
        distance_rate = float(input("Enter distance rate (VNĐ per km): "))
        ll.invoice(weight_rate, distance_rate)
    except ValueError:
        print("Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    main_menu()
