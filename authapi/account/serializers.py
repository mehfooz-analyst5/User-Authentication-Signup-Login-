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




class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name', 'email', 'tc', 'is_admin']



class UserChangePasswordSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=255, style={'input_type':'password'}, write_only=True, trim_whitespace=False)
    password2 = serializers.CharField(max_length=255, style={'input_type':'password'}, write_only=True, trim_whitespace=False)

    class Meta:
        model = User
        fields = ['password', 'password2']
    
    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.get('password2')

        user = self.context.get('user')

        if password != password2:
            raise serializers.ValidationError("Password and Confirm password does'nt match")

        user.set_password(password)
        user.save()
        print('password : ', password)

        return attrs
    