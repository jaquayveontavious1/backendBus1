from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
#from booking.models import School
# Create your models here.


class UserProfile(models.Model) :
    ROLE_CHOICES = [
        ('student','Student'),
        ('parent','Parent'),
        ('bus_manager','Bus_Manager'),
        ('admin','Admin')

    ]
    PAYMENT_METHODS = [
        ('mpesa','Mpesa'),
        ('cash','Cash')
    ]
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    contact_regex = RegexValidator(regex=r'^(?:\+254|254|0)((1|7)(?:(?:[0-9][0-9])|(?:[0-9][0-9][0-9]))[0-9]{6})$',message='Please enter number in the correct format starting with 254 or 01(Upto to 10 digits)')
    contact_number = models.CharField(validators=[contact_regex],max_length=10,verbose_name='Phone number')
    email = models.EmailField(unique=True,blank=True)
    profile_pic = models.ImageField(upload_to='profiles/',blank=True,null=True)
    payment = models.CharField(max_length=255,choices=PAYMENT_METHODS)
    role = models.CharField(max_length=255,choices=ROLE_CHOICES)
    school = models.CharField(max_length=255,null=True,blank=True)

    def __str__(self) :
        return (f"{self.user.username} - {self.firstname} {self.lastname}")
    


    