from django.db import models

# Create your models here.
class students(models.Model):
    stu_id = models.CharField(max_length=200, primary_key=True)
    firstName = models.CharField(max_length=300)
    lastName = models.CharField(max_length=260)
    password = models.CharField(max_length=300)
    batch = models.CharField(max_length=10)
    dept = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=12, default="")
    class Meta:
        db_table = "students"

class posts(models.Model):
    text = models.CharField(max_length=10000)
    student = models.ForeignKey(students, on_delete=models.CASCADE) 
    upvote = models.CharField(max_length=100, null=True, default="0")
    category = models.CharField(max_length=100)
    iid = models.CharField(primary_key=True, max_length=100)

    class Meta:
        db_table = "posts" 
