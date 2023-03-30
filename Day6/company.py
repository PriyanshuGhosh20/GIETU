class Company:
    def __init__(self, name, employee_level_hike):
        self.name = name
        self.employee_level_hike = employee_level_hike
    
    def get_employee_level_hike(self, job_level):
        return self.employee_level_hike.get(job_level, None)

class Employee:
    def __init__(self, name, performance_list):
        self.name = name
        self.performance_list = performance_list
    
    def calculate_salary(self):
        performance_rating = self.performance_list[-1]
        if performance_rating == 1:
            hike_percent = 0
        elif performance_rating == 2:
            hike_percent = 0.02
        else:
            hike_percent = 0.05
        basic_salary = 50000
        hike_amount = basic_salary * hike_percent
        total_salary = basic_salary + hike_amount
        return total_salary

class PermanentEmployee(Employee):
    def __init__(self, name, performance_list, job_level):
        super().__init__(name, performance_list)
        self.job_level = job_level
        self.job_level_hike = {
            "Level 1": 0,
            "Level 2": 0.05,
            "Level 3": 0.1
        }
        self.company_incentive = 5000
        self.employee_incentive = 0
        self.permanent_employee_incentive = 0
    
    def identify_performance_hike(self):
        last_three_years = self.performance_list[-3:]
        if all(rating == 3 for rating in last_three_years):
            return 0.1
        elif all(rating >= 2 for rating in last_three_years):
            return 0.05
        else:
            return None
    
    def identify_job_level_hike(self):
        return self.job_level_hike.get(self.job_level, None)
    
    def identify_incentive(self):
        total_incentive = self.company_incentive + self.employee_incentive + self.permanent_employee_incentive
        return total_incentive
    
    def calculate_salary(self):
        performance_hike_percent = self.identify_performance_hike()
        if performance_hike_percent is None:
            performance_hike_percent = 0
        job_level_hike_percent = self.identify_job_level_hike()
        if job_level_hike_percent is None:
            job_level_hike_percent = 0
        basic_salary = 50000
        hike_amount = basic_salary * (performance_hike_percent + job_level_hike_percent)
        incentive_amount = self.identify_incentive()
        total_salary = basic_salary + hike_amount + incentive_amount
        return total_salary

company = Company("ABC Corp", {"Level 1": 0, "Level 2": 0.05, "Level 3": 0.1})
employee = PermanentEmployee("John", [2, 3, 3, 1, 2], "Level 2")
salary = employee.calculate_salary()
print(salary)
