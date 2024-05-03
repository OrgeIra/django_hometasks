from django.db import models

# Create your models here.

class Teacher_desc(models.Model):
    name = models.CharField(max_length=50)
    last_name =models.CharField(max_length=55)
    age = models.IntegerField(max_length=150)
    gender = models.CharField(max_length=150)
    
    def __str__(self):
        return f"{self.name} {self.last_name} {self.age} {self.gender}"
    
    class Meta:
        db_table = "teacher_desc"