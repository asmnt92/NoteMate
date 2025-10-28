from django.urls import path
from main.views import noteMate

urlpatterns = [
    path('notemate/',noteMate,name='noteMate')
]
