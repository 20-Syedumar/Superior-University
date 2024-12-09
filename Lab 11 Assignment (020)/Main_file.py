import csv
class Employee:
    def __init__(self,name,age,salary):
        self.__name=name
        self.__age=age
        self.__salary=salary

    def get_name(self):
        return self.__name
    def get_age(self):
        return self.__age
    def get_salary(self):
        return self.__salary

    def set_name(self,name):
        self.__name=name
    def set_age(self,age):
        self.__age=age
    def set_salary(self,salary):
        self.__salary=salary 

    def display_info(self):
        print("Name:",self.__name)
        print("Age:",self.__age)
        print("Salary:",self.__salary)


    def to_dic(self):
        return {
            "Name": self.__name,
            "Age": self.__age,
            "Salary": self.__salary
        }
class Manager(Employee):
    def __init__(self, name, age, salary,department):
        super().__init__(name, age, salary)
        self.__department=department
    def get_department(self):
        return self.__department
    def set_department(self,department):
        self.__department=department


    def display_info(self):
        super().display_info()
        print("Department:",self.__department)


    def to_dic(self):
        data=super().to_dic()
        data["Department"]= self.__department
        return data
class Worker(Employee):
    def __init__(self, name, age, salary,hour_worked):
        super().__init__(name, age, salary)
        self.__hour_worked=hour_worked
    def get_hour_worked(self):
        return self.__hour_worked
    def set_hour_worked(self,hour_worked):
        self.__hour_worked=hour_worked
    def display_info(self):
        super().display_info()
        print("Hour Worked:",self.__hour_worked)
    def to_dic(self):
        data=super().to_dic()
        data["Hour Worked"]= self.__hour_worked
        return data

def add_details(detail):
    employee=input("Enter the type of Employee (Manager or Worker): ").strip().lower()
    name=input("Enter the name: ")
    age=int(input("Enter the age: "))
    salary=(int(input("Enter the salary: ")))
    if employee == "manager":
        department=input("Enter the Department:" )
        detail.append(Manager(name,age,salary,department))
    elif employee == "worker":
        hour_worked=int(input("Enter the hour: "))
        detail.append(Worker(name,age,salary,hour_worked))
    else:
        print("--Invalid Type--")

def display_details(detail):
    print()
    for i in detail:
        i.display_info()
        print()

def save_to_csv(detail):

    filename = "Employee_details.csv"


    with open(filename, mode='w', newline='') as file:
        fieldnames = ["Name", "Age", "Salary", "Department", "Hour Worked"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()

        for i in detail:
            writer.writerow(i.to_dic())

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