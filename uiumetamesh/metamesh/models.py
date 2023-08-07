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
    active= models.CharField(max_length=20, default="false")
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

class likes(models.Model):
    counter = models.CharField(max_length=100, default="0", null=True)
    post = models.ForeignKey(posts, on_delete=models.CASCADE)
    user = models.ForeignKey(students, on_delete=models.CASCADE)

    class Meta:
        db_table = 'like'

class notification(models.Model):
    message = models.CharField(max_length=200, default="")
    to = models.ForeignKey(students, on_delete=models.CASCADE)

    class Meta:
        db_table = "notification"

class clubs(models.Model):   
    clubname = models.CharField(max_length=100, primary_key=True)
    clubtype = models.CharField(max_length=100)
    purpose = models.CharField(max_length=200, null=True)
    rules = models.CharField(max_length=200)
    adminname = models.CharField(max_length=100)
    adminid = models.ForeignKey(students, on_delete=models.CASCADE)

    class Meta:
        db_table = 'club'

class clubApproval(models.Model):
    clubid = models.ForeignKey(clubs, on_delete=models.CASCADE)
    studentss = models.ForeignKey(students, on_delete=models.CASCADE)
    status = models.CharField(max_length=100, default="not")
    admin = models.CharField(max_length=100, default="")
    class Meta:
        db_table = "approval"

class clubpost(models.Model):
    clubidd = models.ForeignKey(clubs, on_delete=models.CASCADE)
    student = models.ForeignKey(students, on_delete=models.CASCADE)
    texts = models.CharField(max_length=300, default="")
    iid = models.CharField(max_length=100, primary_key=True)
    upvote = models.CharField(max_length=200, null=True)

    class Meta:
        db_table = "clubpost"