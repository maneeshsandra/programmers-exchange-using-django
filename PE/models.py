from django.db import models

#Create your models here.
class Problem(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=30)
    title=models.CharField(max_length=200)
    difficulty=models.CharField(max_length=10)
    description=models.TextField()
    solution=models.TextField()
    code=models.TextField()
    def __str__(self):
        return self.title

class Contact(models.Model):
    id=models.AutoField(primary_key=True)
    firstname=models.CharField(max_length=30)
    email=models.EmailField()
    mobile=models.CharField(max_length=10)
    message=models.TextField()

    def __str__(self):
        return self.mobile

