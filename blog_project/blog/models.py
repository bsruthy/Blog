from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
	title=models.CharField(max_length=250)
	text=models.TextField()
	created_at=models.DateTimeField(auto_now=True)
	updates_at=models.DateTimeField(auto_now_add=True)
	user=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True,related_name='post')
	views=models.PositiveIntegerField(default=0)

	def __str__(self):
		return self.title


class UserProfile(models.Model):
	user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='user_profile')
	first_name=models.CharField(max_length=250,null=True,blank=True)
	last_name=models.CharField(max_length=250,null=True,blank=True)
	contact_phone=models.CharField(max_length=250,null=True,blank=True)
	profile_pic=models.FileField(upload_to='images/',null=True,blank=True)
	about=models.TextField(max_length=250,null=True,blank=True)

	def __str__(self):
		return str(self.user)