from django.urls import path
from notes.views import test

urlpatterns = [
   path('notes/',test,name='notes')
]
