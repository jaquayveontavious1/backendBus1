from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate

#User Serializer -> It will be used for login by asking the user for username and password
class UserSerializer(serializers.ModelSerializer) :
    class Meta :
        model = User
        fields = ['username','password']


#AuthTokenSerializer -> Store the token for each user

class AuthTokenSerializer(serializers.Serializer) :
    username = serializers.CharField()
    password = serializers.CharField(style={'input_type' : 'password'})

    def validate(self,attrs) :
        username = attrs.get('username')
        password = attrs.get('password')

        if username and password :
            user = authenticate(request=self.context.get('request'),username=username,password=password)

            if not user :
                msg = 'Unable to log in with provided credentials.'
                raise serializers.ValidationError(msg,code='authorization')
            token,created = Token.objects.get_or_create(user=user)
            attrs['user'] = user
            attrs['token'] = token
            return attrs
        else :
            msg = 'Must include "username" and "password"'
            raise serializers.ValidationError(msg,code='authorization')
        

class RegisterSerializer(serializers.ModelSerializer) :
    class Meta :
        model = User
        fields = ['username','email','password']
        extra_kwargs = {'password' : {'write_only' : True}} #it will set in the set that the password has to be typed
    def create(self,validated_data) :
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
        )
        return user