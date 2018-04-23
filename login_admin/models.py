from django.db import models

# Create your models here.

##创建第一个魔豆
class admin(models.Model):
    username = models.CharField(max_length=255)
    groupId = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    last_login_ip = models.CharField(max_length=255)
    last_login_time = models.DateTimeField()
    department = models.IntegerField()
    email = models.CharField(max_length=255)
    realname = models.CharField(max_length=255) 

#    def __str__(self):
#        return admin.username