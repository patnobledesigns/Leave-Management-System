from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class NigeriaState(models.Model):
    state = models.CharField(max_length=100)
    
    def __str__(self):
        return self.state
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    profile_pic = models.ImageField(default='profile1.png', null=True, blank=True)
    Street_Address_Line_1 = models.CharField(max_length=100)
    Street_Address_Line_2 = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    State = models.ForeignKey(NigeriaState, on_delete=models.CASCADE, null=True)
    Postal_code = models.CharField(max_length=50)
    Country = models.CharField(max_length=50, default="Nigerian")
    Mobile_number = models.CharField(max_length=50)
    Nationality = models.CharField(max_length=50)
    Date_Of_Birth = models.CharField(max_length=50)
    
    
    def __str__(self):
        return self.user.username

class LeaveType(models.Model):
    leave_type = models.CharField(max_length=50, null=True)
    
    def __str__(self):
        return self.leave_type
    
class Holiday(models.Model):
    upcoming = models.CharField(max_length=100, null=True)
    
    def __str__(self):
        return self.upcoming
    
class LeaveDetail(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    leave_type = models.ForeignKey(LeaveType, on_delete=models.CASCADE, null=True)
    Begin_Date = models.DateTimeField(default=timezone.now)
    End_Date = models.DateTimeField(default=timezone.now)
    Requesting_Days = models.IntegerField(default=0)
    Reason = models.TextField(max_length=50)
    
    def __str__(self, ):
        return self.Reason
    
    
    
    