<div align="center">

# 👨‍💼 Employee Management System

### Python OOP Project — Inheritance, Encapsulation & Method Overriding

<img src="https://readme-typing-svg.demolab.com?font=Poppins&weight=700&size=28&duration=3000&pause=1000&color=00C2FF&center=true&vCenter=true&width=850&lines=Employee+Management+System;Employee+%7C+Manager+%7C+Developer;Python+Object-Oriented+Programming" alt="Animated Typing Header"/>

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![OOP](https://img.shields.io/badge/Concept-OOP-00C2FF?style=for-the-badge)
![Inheritance](https://img.shields.io/badge/Concept-Inheritance-7C3AED?style=for-the-badge)
![Encapsulation](https://img.shields.io/badge/Concept-Encapsulation-16A34A?style=for-the-badge)

</div>

---

# 🌟 About The Project

**Employee Management System** is a menu-driven Python command-line application for creating and displaying employee, manager, and developer records.

It demonstrates Object-Oriented Programming (OOP): an `Employee` parent class stores common information, while `Manager` and `Developer` inherit from it and add role-specific details.

# 🎯 Project Objectives

- Create employee records
- Create manager records with department details
- Create developer records with programming-language details
- Display all stored records
- Practise encapsulation with private attributes and getter/setter methods
- Demonstrate inheritance and method overriding
- Check class relationships using `issubclass()`

# ✨ Key Features

| Feature | Description |
|---|---|
| 👤 Create Employee | Store ID, name, age, and salary |
| 🧑‍💼 Create Manager | Store employee details and department |
| 💻 Create Developer | Store employee details and programming language |
| 📋 Show Details | Display all records stored during the current run |
| 🔐 Salary Setter | `set_salary()` rejects negative salary values |
| 🧬 Inheritance Check | Check whether `Manager` and `Developer` are subclasses of `Employee` |

# 🧰 Concepts Used

| Concept | Purpose |
|---|---|
| Classes and objects | Represent employees and their roles |
| `__init__()` | Initialise object attributes |
| Encapsulation | Keep employee ID and salary in double-underscore attributes |
| Getters and setters | Access or update employee ID and salary |
| Inheritance | `Manager` and `Developer` inherit from `Employee` |
| Method overriding | Child classes extend `display()` |
| `super()` | Call parent-class constructor and display method |
| `issubclass()` | Check inheritance relationships |
| List | Store employee objects |
| `while` loop | Keep the menu running until Exit is chosen |

# 🏗️ Project Structure

```text
OOP_Wrapper_Project/
├── OOP_Wrapper_Project.py
└── README.md
```

Replace `your_file_name.py` with the actual name of your Python file.

# 🔄 Application Workflow

```text
Start
  |
  v
Display Main Menu
  ├── 1. Create an Employee
  ├── 2. Create a Manager
  ├── 3. Create a Developer
  ├── 4. Show Details
  └── 5. Exit
```

# 📌 Menu Options

| Option | Operation | Description |
|---:|---|---|
| 1 | Create an Employee | Enter ID, name, age, and salary |
| 2 | Create a Manager | Enter employee details and department |
| 3 | Create a Developer | Enter employee details and programming language |
| 4 | Show Details | Display all records in the list |
| 5 | Exit | Close the program |

# 🧬 Understanding Inheritance

```text
          Employee
          /      \
         /        \
    Manager     Developer
```

- **Employee:** Contains ID, name, age, salary, and the common `display()` method.
- **Manager:** Adds a `department` attribute.
- **Developer:** Adds a `language` attribute.
- Both child classes override `display()` and call `super().display()` to display shared details.

# 🔐 Understanding Encapsulation

The class stores employee ID and salary using double-underscore attributes:

```python
self.__emp_id = emp_id
self.__salary = e_salary
```

Getter and setter methods are defined for these attributes. `set_salary()` only accepts a non-negative salary.

**Note:** The menu does not currently call these getter/setter methods. Also, the constructor assigns the initial salary directly, so negative salary input during creation is not blocked by `set_salary()`.

# 💻 Example Main Menu

```text
=== EMPLOYEE MANAGEMENT SYSTEM ===
1. Create an Employee
2. Create a Manager
3. Create a Developer
4. Show Details
5. Exit
Enter your choice (1-5):
```

# 🚀 How to Run

1. Install Python 3.x.
2. Open a terminal in the folder containing your Python file.
3. Run:

```bash
OOP_Wrapper_Project.py
```

OOP_Wrapper_Project.py

# 📋 Requirements

- Python 3.x
- A code editor or terminal (such as VS Code or Command Prompt)
- No third-party libraries required

# 🧠 Skills Practised

- Python OOP
- Classes and objects
- Constructors
- Encapsulation
- Getters and setters
- Inheritance
- Method overriding
- `super()`
- `issubclass()`
- Lists and loops
- Menu-driven application design

# 🔮 Future Enhancements

- Save records using file handling or a database
- Add options to update and delete records
- Search employees by ID or name
- Validate age and salary inputs
- Add employee counts and salary summaries
- Build a graphical user interface
- Add automated tests

# ⚠️ Current Program Notes

- Records are stored in `employees_list` in memory and are not saved permanently.
- The current menu supports creation and display, but not search, update, or delete.
- Numeric inputs for age and salary must be valid.

---

# 👨‍💻 About The Developer

Parth Chauhan

<div align="center">

## 🚀 Keep Learning. Keep Building. Keep Growing.

<img src="https://readme-typing-svg.demolab.com?font=Poppins&weight=600&size=22&duration=3500&pause=1000&color=00C2FF&center=true&vCenter=true&width=700&lines=Learn+OOP.;Build+Useful+Projects.;Keep+Practising+Python." alt="Animated Footer"/>

**Made with ❤️ and Python**

</div>

