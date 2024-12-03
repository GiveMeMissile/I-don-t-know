class Person:
    
    species = "Human (Maybe)"
    
    def __init__(self, sanity, gpa, good_at_math, salary, good_at_science, good_at_reading, happy, name, has_job, age, in_school):
        self.sanity = sanity
        self.gpa = gpa
        self.good_at_math = good_at_math
        self.salary = salary
        self.good_at_science = good_at_science
        self.good_at_reading = good_at_reading
        self.happy = happy
        self.name = name
        self.has_job = has_job
        self.age = age
        self.in_school = in_school
        
    def __str__(self):
        return f"This human's name is {self.name}."
        
    def computer_scientist(self):
        if(not self.good_at_math):
            return False
        if(self.salary <= 100000 or not self.has_job):
            return False
        if(30 < self.sanity):
            return False
        if(self.happy):
            return False
        if(self.gpa < 3.5):
            return False
        return True
    
    def faliure(self):
        fail = False
        fail_results = ""
        if(not self.good_at_math and not self.good_at_science and not self.good_at_reading):
            fail_results += f"{self.name} is not good at any subject. "
            fail = True
        if(self.salary <= 50000 and (not self.in_school or self.age > 20)):
            fail_results += f"{self.name} does not get paid well (Most likely works at mcDonalds). "
            fail = True
        if(not self.in_school and not self.has_job):
            fail_results += f"{self.name} Blud is not in school and is unemployed. Blud is not doing anything of value. "
            fail = True
        if(fail):
            return fail_results
        else:
            return f"{self.name} is not a faliure (:"
        
        
        
Bobby = Person(sanity = 20, gpa = 4, good_at_math = True, salary = 120000, good_at_science = True, good_at_reading = False, happy = False, name = "Bobby", has_job = True, age = 25, in_school = False)
print(Bobby.computer_scientist())
print(Bobby.faliure())
print(Bobby)
        
def harvest_user_info():
    pass

def harvest_other_info():
    pass

def main():
    pass
