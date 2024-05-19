class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def calculate_salary(self):
        return self.salary

class Engineer(Employee):
    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary)
        self.programming_language = programming_language
        
    def write_code(self, coding):
        print(f"{self.name} is writing code in {self.programming_language} ")
        return coding
    
class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def get_department(ManageDepart):
        return self.department
    


class Salesperson(Employee):
    def __init__(self, name, salary, total_sales=0):
        super().__init__(name, salary)
        self.total_sales = total_sales
        

    def get_sales_made(self):
        return self.total_sales
    

    def add_sale(self, amount):
        if not isinstance(int, float):
            raise TypeError("Sales is not anumber")
        self.total_sales += amount

Employee('Jacob', 10000)
Engineer('James', 10000, 'python')
Manager('Daryl', 20000, 'Manager of Computer Engineer')
Salesperson('Anthony', 5000, 5)

