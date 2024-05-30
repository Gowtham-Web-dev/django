from django.urls import path,include
from Level5_pro import views
app_name="Level5_pro"
urlpatterns=[
 path("login",views.user_login,name="login"),
 path("register",views.register,name="register"),


]