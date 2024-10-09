from django.urls import path
from .views import *

app_name = 'couplers'

urlpatterns = [
    path('', home, name = "home"),
    path('thank-you', thank_you, name='thank_you')
]
