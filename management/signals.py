from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from .models import *



def customer_profile(sender, instance, created, **kwargs):
	if created: 
		group = Group.objects.get(name='Staff')
		instance.groups.add(group)
		
		# Profile.objects.create(user=instance)
		# LeaveDetail.objects.create(profile=instance)
		# new_user = LeaveDetail()
		# new_user.user = instance
		print('Profile created!')

post_save.connect(customer_profile, sender=User)