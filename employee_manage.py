class Employee:
    def __init__(self,id,name,age,salary):
        self.__emp_id = id
        self.emp_name = name
        self.age = age
        self.__salary = salary

     
    def set_id(self,id):
        self.__emp_id = id

    def get_id(self):
        return self.__emp_id


    def set_salary(self,salary):
        self.__salary = salary

    def get_salary(self):
        return self.__salary


    def display(self):
        print(f"Id         : {self.__emp_id}")
        print(f"Name       : {self.emp_name}")
        print(f"Age        : {self.age}")
        print(f"Salary     : {self.__salary}")

    def __del__(self):
        pass
class Manager(Employee):
    def __init__(self,id,name,age,salary,department):
        super().__init__(id,name,age,salary)
        self.department = department
    def display(self):
        super().display()
        print(f"Department : {self.department}")

class Developer(Employee):
    def __init__(self,id,name,age,salary,pro_language):
        super().__init__(id,name,age,salary)
        self.pro_lan = pro_language
    def display(self):
        super().display()
        print(f"Programming Language : {self.pro_lan}")

emp = []
man  = []
dev = []
while True:
   
    print("\n1.Create Employee")
    print("2.Create Manager")
    print("3.Create Developer")
    print("4.Show Details")
    print("5.Update Salary")
    print("6.Exit\n")


    choice = int(input("Enter your choice :"))

    match(choice):
        case 1:
            id = int(input("Enter id:"))
            name = input("Enter name:")
            age = int(input("Enter age:"))
            salary = int(input("Enter salary:"))
            emp.append(Employee(id,name,age,salary))

            print("\nEmployee is created...\n")

        case 2:
            id = int(input("Enter id:"))
            name = input("Enter name:")
            age = int(input("Enter age:"))
            salary = int(input("Enter salary:"))
            department = input("Enter Department : ")
            man.append(Manager(id,name,age,salary,department))
            print("\nManager is created.....\n")

        case 3:
            id = int(input("Enter id:"))
            name = input("Enter name:")
            age = int(input("Enter age:"))
            salary = int(input("Enter salary:"))
            pro_l = input("Enter Programming Language :")
            dev.append(Developer(id,name,age,salary,pro_l))
            print("\nDeveloper is created....\n")

        case 4:
            sub_class = issubclass(Manager,Employee)
            sub_class1 = issubclass(Developer,Employee)

            if sub_class == True and sub_class1 == True:
                print("\nManager and Developer are subclasses of Employee class. \n")
            else:
                pass


            while True:
                

                print("\n======Show Details=====")
                print("1.Employee")
                print("2.Manager")
                print("3.Developer")
                print("4.Exit")
                c = int(input("Enter your choice :"))
                if c == 1:
                    if emp:
                        for i,e in enumerate(emp,1):
                            print(f"\n===============Employee {i}===============")
                            e.display()
                    else:
                        print("\nEmployee not available")
                elif c == 2:
                    if man:
                        for i,m in enumerate(man,1):
                            print(f"\n===============Manager {i}================")
                            m.display() 
                        
                    else:
                        print("\nManager not available")
                elif c == 3:
                    if dev: 
                        for i,d in enumerate(dev,1):
                            print(f"===============Developer {i}===================")
                            d.display()
                    else:
                        print("\nDeveloper not available")
                elif c == 4:
                    break
                else:
                    print("invalid choice")
        case 5:
            print("\n1.Employee Salary")
            print("2.Manager Salary")
            print("3.Developer Salary\n")

            c = int(input("Enter Your choice:"))
            if c == 1:
                eid = int(input("Enter Employee Id:"))

                for e1 in emp:
                    if e1.get_id() == eid:
                        new_salary = int(input("Enter New Salary :"))
                        e1.set_salary(new_salary)
                        print("\nEmployee salary updated successfully......\n")
                        break
                else:
                    print("Employee id not found")
            elif c == 2:
                mid = int(input("Enter Manager Id : "))

                for m in man:
                    if m.get_id() == mid:
                        new_salary = int(input("Enter new Salary : "))
                        m.set_salary(new_salary)
                        print("\nManager salary updated successfully......\n")
                        break
                else:
                    print("Manager id not found...")
            elif c == 3:
                d_id = int(input("Enter Developer Id : "))

                for d in dev:
                    if d.get_id() == d_id:
                        new_salary = int(input("Enter new Salary : "))
                        d.set_salary(new_salary)
                        print("\nDeveloper salary updated successfully......\n")
                        break
                else:
                    print("Developer id not found...")
            else:
                print("invalid choice")
        case 6:
            break

        case _:
            print("Invalid choice")
