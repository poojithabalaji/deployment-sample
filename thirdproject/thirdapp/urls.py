from thirdapp import views
from django.urls import path,include


urlpatterns =[
    path('',views.users,name='users')
]
