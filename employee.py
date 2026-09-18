class Salary:
    employee_id="10405"
    name="Karthik"
    basic_salary=100000
    def totalsalary(self):
        HRA=0.2*self.basic_salary
        DA=0.1*self.basic_salary
        total=HRA+DA+self.basic_salary
        print("Employee ID:",self.employee_id)
        print("Name:",self.name)
        print("Basic Salary:",self.basic_salary)
        print("HRA:",HRA)
        print("DA:",DA)
        print("Total Salary:",total)
d = Salary()
d.totalsalary()
