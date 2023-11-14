from django.urls import path
from . import views 

app_name = 'accounts'
urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name="logout"),
    path('signup/', views.signup, name="signup"),
    path('cancelAccount/', views.cancelAccount, name="cancelAccount"),
    path('update/', views.update, name='update'),
]

