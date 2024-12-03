class Why:
    def __init__(self, sanity, GPA, good_at_math, salary, good_at_science, good_at_reading, happy, name):
        self.sanity = sanity
        self.GPA = GPA
        self.good_at_math = good_at_math
        self.salary = salary
        self.good_at_science = good_at_science
        self.good_at_reading = good_at_reading
        self.happy = happy
        self.name = name
        
    def computer_scientist(x):
        if(not self.good_at_math):
            return False
        if(self.salary >= 50000):
            return False
        if(30 < self.sanity):
            return False
        if(not self.happy):
            return False
        if(self.GPA < 3.5):
            return False
        return True


Bobby = Why(sanity = 20, GPA = 4, good_at_math = True, salary = 120000, good_at_science = True, good_at_reading = False, happy = False, name = "Bobby")
x = Bobby.computer_scientist()
print(x)
