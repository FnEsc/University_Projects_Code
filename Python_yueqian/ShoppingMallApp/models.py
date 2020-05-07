from django.db import models

# Create your models here.

class Userinfo(models.Model):
    #如果没有models.AutoField，默认会创建一个id的自增列,且primary_key=True
    username = models.CharField(max_length=50,null=False)
    password = models.CharField(max_length=50)

