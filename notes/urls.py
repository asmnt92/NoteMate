from django.urls import path
from notes.views import dashboard,edit,delete
app_name = 'notes'
urlpatterns = [
   path('notes/',dashboard,name='notes'),
   path('edit/<int:id>/',edit,name='edit'),
   path('delete/<int:id>/',delete,name='delete')
]
