from django.db import models


# Create your models here.
class Student(models.Model):
    roll_no = models.TextField()
    name = models.TextField(max_length=40)
    std_class = models.TextField()
    dept = models.TextField()
    year = models.TextField(default='null')
    def __str__(self):
        return self.name

class Subject(models.Model):
    roll_no = models.TextField()
    name = models.TextField(max_length=40)
    dept = models.TextField()


class Book(models.Model):
    name = models.CharField(max_length = 50)
    picture = models.ImageField()
    author = models.CharField(max_length = 30, default='anonymous')
    email = models.EmailField(blank = True)
    describe = models.TextField(default = 'CRUD Django tutorials')
    student = models.ManyToManyField(Student)
    def __str__(self):
        return self.name




