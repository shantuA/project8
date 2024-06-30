from django.urls import path
from app2.views import *
app_name='brahma'

urlpatterns=[

    path('operator/',operator,name='operator'),
]