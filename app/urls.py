from django.urls import path
from app.views import *
app_name='shiva'

urlpatterns=[
    path('distroyer/',distroyer,name='distroyer')
]