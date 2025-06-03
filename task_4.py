class EmployeeSalary:
    hourly_payment = 400

    def __init__(self, name, hours=None, rest_days=None, email=None):
        self.name = name 
        self.hours = hours
        self.rest_days = rest_days
        self.email = email

    def get_hours(self):
        if self.hours is None:
            if self.rest_days is None:
                return 0
            return (7 - self.rest_days) * 8 
        return self.hours

    def get_email(self):
        if self.email is None:
            return f"{self.name.lower().replace(' ', '.')}@email.com"
        return self.email
    
    @classmethod
    def set_hourly_payment(cls, new_rate):
        cls.hourly_payment = new_rate
  
    def salary(self):
        fact_hours = self.get_hours()
        return fact_hours * self.hourly_payment 