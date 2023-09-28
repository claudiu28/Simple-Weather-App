from . import views as vws
from django.urls import path


urlpatterns = [
    path('', vws.WeatherApp, name='WeatherApp'),
]

