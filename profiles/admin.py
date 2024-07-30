from django.contrib import admin
from .models import UserProfile
# Register your models here.
class UserProfileAdmin(admin.ModelAdmin) :
    list_display = ('firstname','lastname','contact_number','email','profile_pic','payment','role','school')
    search_fields = ('firstname','lastname','contact_number','email')


admin.site.register(UserProfile,UserProfileAdmin)