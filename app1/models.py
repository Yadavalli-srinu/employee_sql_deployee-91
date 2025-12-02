from django.db import models

class employee_model(models.Model):
    emp_name=models.CharField(max_length=50)
    emp_id=models.IntegerField(unique=True)
    emp_mobile=models.BigIntegerField()
    emp_salary=models.IntegerField()
