from home.models import User
from rest_framework import serializers



class UserListAdminSerializer(serializers.ModelSerializer):
     class Meta:
          model = User
          fields = ['id','first_name','last_name','username','email','password','blocked','is_active','created_at','updated_at','is_doctor']

class UserProfileAdminSerializer(serializers.ModelSerializer):
     class Meta:
          model = User
          fields = ['first_name','last_name','username','email','blocked','is_doctor']
          
          
class DoctorListAdminSerializer(serializers.ModelSerializer):
     class Meta:
          model = User
          fields = ['id','first_name','last_name','username','email','password','blocked','is_active','is_doctor','created_at','updated_at']


class DoctorProfileAdminSerializer(serializers.ModelSerializer):
     class Meta:
          model = User
          fields = ['first_name','last_name','username','email','blocked','is_doctor']