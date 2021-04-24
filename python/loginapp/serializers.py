from rest_framework import serializers

from .models import Users


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['u_id', 'u_gender', 'u_pwd', 'u_name','u_age','u_email']

