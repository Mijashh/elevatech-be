from rest_framework import serializers

from .models import User, UserRoles


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    username = serializers.CharField(source='name') 
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'role']
        extra_kwargs = {
            'password': {'write_only': True},
            'role': {'required': True}
        }
    
    def validate_role(self, value):
        if value not in [UserRoles.STUDENT, UserRoles.COMPANY]:
            raise serializers.ValidationError("Invalid role selected")
        return value

    
