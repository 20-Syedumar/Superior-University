import csv
from File_2 import Premium
from File_3 import Normal
# Cell 4: Main Program
def add_details(detail):
    service = input("Enter service type (Premium/Normal): ").strip().lower()
    name = input("Enter name: ")
    day = int(input("Enter the number of Days: "))
    number = int(input("Enter the contact Number: "))
    room_num = int(input("Enter the Room Number 0-100: "))

    if service == 'premium':
        extra = input("Add breakfast (YES/No): ")
        detail.append(Premium(name, day, number, room_num, service, extra))
    else:
        detail.append(Normal(name, day, number, room_num, service))


def display_details(detail):
    print()
    for i in detail:
        i.display_info()
        print()


def save_to_csv(detail):
    # Define the CSV file name
    filename = "guest_details.csv"

    # Open the file in write mode
    with open(filename, mode='w', newline='') as file:
        fieldnames = ["Name", "Day", "Number", "Room Number", "Service", "Breakfast"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        # Write header (if file is empty)
        writer.writeheader()

        # Write guest data to CSV
        for guest in detail:
            writer.writerow(guest.to_dict())

    print(f"Details saved to {filename}")


def main():
    detail = []

    while True:
        print("1. Add Detail")
        print("2. Display Detail")
        print("3. Save Details to CSV")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            add_details(detail)
        elif choice == 2:
            display_details(detail)
        elif choice == 3:
            save_to_csv(detail)
        elif choice == 4:
            print("--Exiting--")
            break
        else:
            print("Invalid choice! Please try again.")


if __name__ == '__main__':
    main()