from django.urls import path
from . views import UserListAdminView,DoctorListAdminView,UserProfileAdminView,DoctorProfileAdminView

urlpatterns = [

    path('user/',UserListAdminView.as_view(),name='user'),
    path('doctor/',DoctorListAdminView.as_view(),name='user'),
    path('user/update/<int:pk>/',UserProfileAdminView.as_view(),name='user'),
    path('doctor/update/<int:pk>/',DoctorProfileAdminView.as_view(),name='user'),
]