from django.db import models


class User(models.Model):

    username = models.CharField(max_length=15,blank=False, null=False)

    name = models.CharField(max_length=25,blank=False, null=False,default="")

    dob = models.CharField(max_length=10,blank=False, null=False,default="")
    email = models.CharField(max_length=25,blank=False, null=False,default="")

    roll = models.CharField(max_length=10,blank=False, null=False,default="")
    phone = models.CharField(max_length=12,blank=False, null=False,default="")
    department = models.CharField(max_length=25,default="",blank=False, null=False)

    password = models.CharField(max_length=13,blank=False, null=False)
    password1 = models.CharField(max_length=13,blank=False, null=False,default="")


    def __str__(self):
        return self.username
