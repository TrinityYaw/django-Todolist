from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser


class Task(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    title = models.CharField(max_length=200)
    description = models.TextField(null=False,blank=True)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        
        return self.title
    
    class Meta:
        verbose_name = "Task"
        verbose_name_plural = "Task"
        ordering = ['complete']
        
