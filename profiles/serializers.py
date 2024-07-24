from rest_framework import serializers
from profiles.models import UserProfile
#from booking.models import School
class UserProfileSerializer(serializers.ModelSerializer) :
    #school = serializers.PrimaryKeyRelatedField(queryset=School.objects.all())

    class Meta :
        model = UserProfile
        fields = ['firstname','lastname','contact_number','email','profile_pic','payment','role','school']
        read_only_fields = ['id','user']


    def create(self,validate_data) :
        user = self.context['request'].user
        validate_data.pop('user',None)
        print(validate_data)
        user_profile = UserProfile.objects.create(user=user,**validate_data)
        return user_profile