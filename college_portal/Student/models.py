from django.db import models

class Student_table(models.Model):
    reg_no=models.IntegerField(primary_key=True)
    name=models.CharField()
    email=models.EmailField()
    dob=models.DateField()
    marks=models.DecimalField(max_digits=6,decimal_places=2)
    
   
