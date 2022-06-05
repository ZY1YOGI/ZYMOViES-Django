from django.urls import path
from .           import views


urlpatterns = [
    path('SignUp/', views.SignUp_SignUp,                        name ='SignUp-SignIn'),
    path('Logout/', views.LogoutUser,                            name ='Logout'),
    path('Profile/',views.profile,                               name ='Profile'),
    path('password-change/', views.ChangePasswordView.as_view(), name='password_change'),
    path('<slug:slug>', views.Profiles_Users,                    name='Profiles_Users'),
]