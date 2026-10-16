class Employee:
    
    def __init__(self, emp_id=None, e_name="", e_age=0, e_salary=0.0):
        
        self.__emp_id = emp_id
        self.e_name = e_name
        self.e_age = e_age
        self.__salary = e_salary

    # Getter and Setter for emp_id
    def get_emp_id(self):
        return self.__emp_id

    def set_emp_id(self, emp_id):
        self.__emp_id = emp_id

    # Getter and Setter for salary
    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        if salary >= 0:
            self.__salary = salary
        else:
            print("Salary cannot be negative.")

    
    def display(self):
        print("Employee ID:", self.__emp_id)
        print("Name:", self.e_name)
        print("Age:", self.e_age)
        print("Salary:", self.__salary)

    def __del__(self):
        pass


class Manager(Employee):
    def __init__(self, emp_id=None, e_name="", e_age=0, e_salary=0.0, department=""):
        super().__init__(emp_id, e_name, e_age, e_salary)
        self.department = department

    def display(self):
        super().display()
        print("Department :", self.department)


class Developer(Employee):

    def __init__(self, emp_id=None, e_name="", e_age=0, e_salary=0.0, language=""):
        super().__init__(emp_id, e_name, e_age, e_salary)
        self.language = language

    def display(self):
        super().display()
        print("Language   :", self.language)


print("Is Manager a subclass of Employee?  :", issubclass(Manager, Employee))
print("Is Developer a subclass of Employee?:", issubclass(Developer, Employee))

employees_list = []


while True:
    print("\n=== EMPLOYEE MANAGEMENT SYSTEM ===")
    print("1. Create an Employee")
    print("2. Create a Manager")
    print("3. Create a Developer")
    print("4. Show Details")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ").strip()

    if choice == "1":
        emp_id = input("Enter Employee ID: ")
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        salary = float(input("Enter Salary: "))
        emp = Employee(emp_id, name, age, salary)
        employees_list.append(emp)
        print("Employee created successfully!")

    elif choice == "2":
        emp_id = input("Enter Employee ID: ")
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        salary = float(input("Enter Salary: "))
        dept = input("Enter Department: ")
        mgr = Manager(emp_id, name, age, salary, dept)
        employees_list.append(mgr)
        print("Manager created successfully!")

    elif choice == "3":
        emp_id = input("Enter Employee ID: ")
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        salary = float(input("Enter Salary: "))
        lang = input("Enter Programming Language: ")
        dev = Developer(emp_id, name, age, salary, lang)
        employees_list.append(dev)
        print("Developer created successfully!")

    elif choice == "4":
        if not employees_list:
            print("No records available to display.")
        else:
            print("\n--- Displaying All Records ---")
            for emp in employees_list:
                print("---------------------")
                emp.display()

    elif choice == "5":
        print("Exiting program. Thank you!")
        break

    else:
        print("Invalid choice, please select between 1 and 5.")