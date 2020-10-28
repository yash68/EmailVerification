from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class MyProfile(models.Model):

	user = models.ForeignKey(User, on_delete=models.CASCADE)
	full_name = models.CharField(max_length=50)
	city = models.CharField(max_length=50)
	contact_no = models.IntegerField()
	email = models.EmailField()

	def save(self, *args, **kwargs):
		if not self.email:
			self.email = self.user.email
		super(MyProfile, self).save(*args, **kwargs)