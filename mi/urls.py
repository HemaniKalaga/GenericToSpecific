from mi.views import *
from django.urls import path
app_name='2'

urlpatterns=[

    path('miteam1/',miteam1,name='miteam1'),
    path('miteam2/',miteam2,name='miteam2'),
]