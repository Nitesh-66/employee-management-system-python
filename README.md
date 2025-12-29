
# Employee Management System (Python)

## Project Description

This project is a menu-driven Employee Management System developed using Python and Object-Oriented Programming (OOP) concepts.

It allows users to create Employees, Managers, and Developers, display their details, and update salaries. The program runs in the terminal and stores data temporarily using lists.

---

## Features

* Create Employee, Manager, and Developer
* Display details in proper format
* Update salary using ID
* Menu-driven program
* Uses Object-Oriented Programming concepts
* Demonstrates inheritance and encapsulation
* Method overriding is used

---

## Classes Used

### Employee Class

* Attributes: ID, Name, Age, Salary
* Methods:

  * set_id(), get_id()
  * set_salary(), get_salary()
  * display()

### Manager Class

* Inherits from Employee
* Additional attribute: Department
* Overrides display() method

### Developer Class

* Inherits from Employee
* Additional attribute: Programming Language
* Overrides display() method

---

## How to Run

### Requirements

* Python 3.10 or higher

### Steps

1. Download or clone the repository
2. Open terminal or command prompt
3. Navigate to the project directory
4. Run the program using:

```bash
python employee_manage.py
```

---

## Menu Options

1. Create Employee
2. Create Manager
3. Create Developer
4. Show Details
5. Update Salary
6. Exit

---

## Sample Output

* Displays employee, manager, and developer details
* Shows success messages after creation and salary update
* Displays error message if ID is not found

