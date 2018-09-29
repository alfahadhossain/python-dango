from django.db import models

# Create your models here
class StudentManager(models.Model):
    def adults(self):
        std_list = Studentinfo.object.filter(age__gte=15)
        return std_list

class Studentinfo(models.Model):
    fast_name= models.CharField(max_length=50)
    last_name= models.CharField(max_length=50)
    age=models.IntegerField()

    object = StudentManager()

    def full_name(self):
        return self.fast_name+' '+self.last_name

    def __str__(self):
        return self.fast_name
