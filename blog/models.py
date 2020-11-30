from django.db import models

# Create your models here.

class Donate(models.Model):
    donate_id = models.AutoField(primary_key=True)
    fname = models.CharField(max_length=50,default="")
    lname = models.CharField(max_length=50,default="")
    email = models.CharField(max_length=70, default="")
    address= models.CharField(max_length=70, default="")
    country = models.CharField(max_length=50, default="")


    def __str__(self):
        return self.fname

class Feedback(models.Model):
    feed_id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=70, default="harsh@xyz.com")
    desc = models.CharField(max_length=500, default="")

    def __str__(self):
        return self.email
    
class Pets(models.Model):
    pet_id = models.AutoField
    pet_name = models.CharField(max_length=50)
    breead = models.CharField(max_length=50, default="")
    age = models.IntegerField(default=0)
    desc = models.CharField(max_length=300)
    pub_date = models.DateField()
    image = models.ImageField(upload_to='blog/images', default="")

    def __str__(self):
        return self.pet_name


