from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser,IsAuthenticated
from home.models import User
from home.serializers import UserLoginSerializer
from .serializers import UserProfileAdminSerializer,DoctorProfileAdminSerializer,UserListAdminSerializer,DoctorListAdminSerializer
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class UserListAdminView(APIView):
     permission_classes=[IsAdminUser,IsAuthenticated]

     def get(self,request,format=None):
          users = User.objects.filter(is_admin=False,is_doctor=False)
          serializer = UserListAdminSerializer(users, many=True)
          data ={
               'msg':'User List',
               'Data':serializer.data
          }
          return Response(data,status=status.HTTP_200_OK)



class DoctorListAdminView(APIView):
     permission_classes=[IsAdminUser,IsAuthenticated]
     
     def get(self, request,format=None):
          users = User.objects.filter(is_doctor=True,is_admin=False)
          serializer = DoctorListAdminSerializer(users, many=True)
          data = {
            "detail": "doctor list",
            "data": serializer.data
        }
          return Response(data,status=status.HTTP_200_OK)


class UserProfileAdminView(APIView):
     permission_classes=[IsAdminUser,IsAuthenticated]
     def get(self, request,pk,format=None):
     
        try:
            users = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response({'msg':'User id dose not exist'},status=status.HTTP_404_NOT_FOUND)
        serializer = UserProfileAdminSerializer(users)
        return Response(serializer.data,status=status.HTTP_200_OK)
        
            
     def put(self, request,pk,format=None):
         
          try:
               users = User.objects.get(pk=pk)
               serializer = UserProfileAdminSerializer(users,data=request.data,partial=True)
               if serializer.is_valid():
                    serializer.save()
                    return Response({"msg":"Data Updated "},status=status.HTTP_200_OK)
               else:
                    return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)
          except User.DoesNotExist:
               return Response({'msg':'User id Dose not exist'},status=status.HTTP_404_NOT_FOUND)
     
     def delete(self,request,pk,format=None):
        
          try:
               user = User.objects.get(pk=pk)
               user.delete()
               return Response({'msg':'Data Deleted'})
          except User.DoesNotExist:
               return Response({'msg':'User id dose not exist'},status=status.HTTP_404_NOT_FOUND)





class DoctorProfileAdminView(APIView):
     permission_classes=[IsAdminUser,IsAuthenticated]
     
     def get(self, request,pk,format=None):
          try:
               users = User.objects.get(pk=pk)
               serializer = DoctorProfileAdminSerializer(users)
          except User.DoesNotExist:
               return Response({'msg':'Doctor id dose not exist'},status=status.HTTP_404_NOT_FOUND)
          return Response(serializer.data)
     
     def put(self, request,pk,format=None):
        
          try:
               users = User.objects.get(pk=pk)
               serializer = UserProfileAdminSerializer(users,data=request.data,partial=True)
               if serializer.is_valid():
                    serializer.save()
                    return Response({"msg":"Data Updated "},status=status.HTTP_200_OK)
               else:
                    return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)
          except User.DoesNotExist:
               return Response({'msg':'Doctor id dose not exist'},status=status.HTTP_404_NOT_FOUND)
     
     def delete(self,request,pk,format=None):
          
          try:
               user = User.objects.get(pk=pk)
               user.delete()
               return Response({'msg':'Data Deleted'},status=status.HTTP_200_OK)
          except User.DoesNotExist:
               return Response({'msg':'Doctor id dose not exist'},status=status.HTTP_404_NOT_FOUND)