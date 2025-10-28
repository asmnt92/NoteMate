from django.urls import path
from home.views import home_page
app_name='home'
urlpatterns = [
    path('guest',home_page,name='guest-page')
]
