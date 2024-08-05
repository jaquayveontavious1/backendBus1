from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
import qrcode
from io import BytesIO
from django.core.files import File
# Create your models here.


class School(models.Model) :
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    school_image = models.ImageField(upload_to='school_pictures/',null=True,blank=True)
    contact_regex = RegexValidator(regex=r'^\+254\s?[7|0][0-9]{2}\s?[0-9]{3}\s?[0-9]{3}$',message="Phone number must be entered in the format: +254123456789 or +254 123 456 789 (up to 10 digits).")
    contact_number = models.CharField(validators=[contact_regex],max_length=15,verbose_name='Phone number')
    email = models.EmailField()
    principal_name = models.CharField(max_length=255)
    students_count = models.PositiveIntegerField()
    created_at = models.DateField(auto_now=True)
    updated_at = models.DateField(auto_now=True)


    def __str__(self) :
        return(f"{self.name}")



class Route(models.Model) :
    route_number = models.CharField(max_length=20)
    image = models.ImageField(upload_to='route_pictures/')
    starting_location = models.CharField(max_length=255)
    final_destination = models.CharField(max_length=255)
    departure_date = models.DateTimeField()
    estimated_arrival = models.DateTimeField()
    distance_covered = models.CharField(max_length=255)
    cost = models.CharField(max_length=15)
    school = models.ManyToManyField(School)

    def __str__(self) :
        return (f"{self.starting_location} to {self.final_destination} ")


class Bus(models.Model) :
   
    bus_number = models.CharField(max_length=255)
    capacity = models.PositiveIntegerField()
    type = models.CharField(max_length=30)
    
    license_plate = models.CharField(max_length=255)
    route = models.ForeignKey(Route,on_delete=models.CASCADE)
     
    def __str__(self) :
        return (f"{self.bus_number} for {self.route}")

class Seat(models.Model) :
    seat_number = models.CharField(max_length=100)
    is_available = models.BooleanField(default=True)
    bus = models.ForeignKey(Bus,on_delete=models.CASCADE,related_name='seats')
    route = models.ForeignKey(Route,on_delete=models.SET_NULL,null=True,blank=True)
    booked_by = models.ForeignKey(User,on_delete=models.SET_NULL,blank=True,null=True)

    def __str__(self) :
        return(f"Seat : {self.seat_number} in {self.bus.bus_number}")
class Driver(models.Model) :
    name = models.CharField(max_length=200)
    license_number = models.PositiveIntegerField()
    contact_regex = RegexValidator(regex=r'^(\+254)?[ ]?[7]{1}([0-9]{1})([0-9]{1})[ ]?[0-9]{3}[ ]?[0-9]{3}$',message="Phone number must be entered in the format: +254123456789 or +254 123 456 789 (up to 10 digits).")
    contact_number = models.CharField(validators=[contact_regex],max_length=15,verbose_name='Phone number')
    image = models.ImageField(upload_to='driver_pictures/')
    email_address = models.EmailField()
    emerg_cont_name = models.CharField(max_length=200)
    emerg_cont_regex = RegexValidator(regex=r'^(\+254)?[ ]?[7]{1}([0-9]{1})([0-9]{1})[ ]?[0-9]{3}[ ]?[0-9]{3}$',message="Phone number must be entered in the format: +254123456789 or +254 123 456 789 (up to 10 digits).")
    emerg_cont_no = models.CharField(validators=[emerg_cont_regex],max_length=15,verbose_name='Phone number')
    bus = models.ForeignKey(Bus,on_delete=models.CASCADE)
    employment_date = models.DateField()
    created_at = models.DateField(auto_now=True)
    updated_at = models.DateField(auto_now=True)
    route = models.ManyToManyField(Route)

    def __str__(self) :
        return (f'{self.name}')

class Booking(models.Model) :
    STATUS_CHOICES = [
        ('pending','Pending'),
        ('cancelled','Cancelled'),
        ('confirmed','Confirmed')
    ]
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    bus = models.ForeignKey(Bus,on_delete=models.CASCADE)
    route = models.ForeignKey(Route,on_delete=models.CASCADE)
    seat = models.ForeignKey(Seat,on_delete=models.CASCADE)
    contact_regex = RegexValidator(regex=r'^(\+254)?[ ]?[7]{1}([0-9]{1})([0-9]{1})[ ]?[0-9]{3}[ ]?[0-9]{3}$',message="Phone number must be entered in the format: +254123456789 or +254 123 456 789 (up to 10 digits).")
    contact_number = models.CharField(validators=[contact_regex],max_length=15,verbose_name='Phone number',null=True,blank=True)
    booking_date = models.DateField()
    total_amount = models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True)
    payment_status = models.CharField(max_length=100,choices=STATUS_CHOICES,default='Pending')
    school = models.ForeignKey(School,on_delete=models.CASCADE)
    qr_code = models.ImageField(upload_to='booking_qr/',null=True,blank=True)
    


    def save(self,*args,**kwargs) :
        qr_image = qrcode.make(f"Booking ID :{self.id}\nUser:{self.user}\nRoute: {self.route} ")
        buffer = BytesIO()
        qr_image.save(buffer)
        filebuffer = File(buffer,name=f'qr_code_{self.id}.png')
        self.qr_code.save(f'qr_code_{self.id}.png',filebuffer,save=False)
        super().save(*args,**kwargs)
    def __str__(self) :
        return (f"{self.user} in {self.bus}")


class Payment(models.Model) :

    PAYMENT_METHODS = [
        ('Debit Card','debit card'),
        ('Credit Card','credit card'),
        ('Mpesa','mpesa')
    ]
    PAYMENT_STATUS = [
        ('pending','Pending'),
        ('cancelled','Cancelled'),
        ('confirmed','Confirmed')
    ]
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    booking = models.ForeignKey(Booking,on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10,decimal_places=2)
    payment_method = models.CharField(max_length=255,choices=PAYMENT_METHODS)
    payment_date = models.DateField()
    status = models.CharField(max_length=255,choices=PAYMENT_STATUS)
    

    def __str__(self) :
        return (f'{self.user}')
