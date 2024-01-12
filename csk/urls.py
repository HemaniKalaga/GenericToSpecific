

from csk.views import *
from django.urls import path
app_name='1'

urlpatterns=[

    path('msd1/',msd1,name='msd1'),
    path('msd2/',msd2,name='msd2'),
]