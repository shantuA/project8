from django.urls import path
from app1.views import *
app_name='vishnu'

urlpatterns=[
    path('creator/',creator,name='creator')
]