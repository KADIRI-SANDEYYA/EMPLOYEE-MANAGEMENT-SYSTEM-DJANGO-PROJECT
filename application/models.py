from django.db import models

# Create your models here.
class EmployeeModel(models.Model):
    employee_id = models.IntegerField(unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone = models.BigIntegerField(unique=True)
    DEPARTMENT_CHOICE = [('IT','IT'),('SALES','SALES'),('HR','HR'),('FINANCE','FINANCE'),('MARKETING','MARKETING')]
    department = models.CharField(max_length=50,choices=DEPARTMENT_CHOICE)
    DESIGNATION_CHOICE = [('Python Developer','Python Developer'),('Java Developer','Java Developer'),('AI Engineer','AI Engineer'),('ML Engineer','ML Engineer'),('Devops Engineer','Software Developer'),('Backend Developer','Backend Developer'),('Frontend Developer','Frontend Developer')]
    designation = models.CharField(max_length=50,choices=DESIGNATION_CHOICE)
    salary = models.DecimalField(max_digits=10,decimal_places=2)
    joining_date = models.DateField()
    profile_image = models.ImageField(upload_to='images/')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"