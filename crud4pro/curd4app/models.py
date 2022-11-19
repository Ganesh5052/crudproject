from django.db import models

class EmployeeData(models.Model):
    employee_id = models.IntegerField()
    employee_name = models.CharField(max_length = 50)
    salary = models.IntegerField()
    experience = models.IntegerField()
    location = models.CharField(max_length = 50)
