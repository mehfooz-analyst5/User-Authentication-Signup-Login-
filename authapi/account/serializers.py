from rest_framework import serializers
from .models import User



class UserRegistrationSerializer(serializers.ModelSerializer):

    password2 = serializers.CharField(style={'input_type':'password'}, write_only=True, trim_whitespace=False)

    class Meta:
        model = User
        fields = ['name', 'email', 'tc', 'password', 'password2']
        extra_kwargs = {
            'password' : {'write_only':True}
        }

    """
    Validating Password & confirm password while registration.
    """

    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.get('password2')
        print(password, password2)

        if password != password2:
            raise serializers.ValidationError("Password and Confirm password does'nt match")

        return attrs
    
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)




class UserLoginSerializer(serializers.ModelSerializer):
    email = serializers.CharField(max_length=255)

    class Meta:
        model = User
        fields = ['email', 'password']