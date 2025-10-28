from django.shortcuts import render,redirect
from django.http import HttpResponse
from notes.models import Notes
from notes.forms import NotesForm

# Create your views here.
def dashboard(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            title=request.POST.get('title')
            note=request.POST.get('description')
            Notes.objects.create(title=title,note=note)
            return redirect('notes:notes')
            
        search=request.GET.get('search')
        notes=Notes.objects.all()
        count=notes.count()
        if search:
            notes=Notes.objects.filter(title__icontains=search)
            count=notes.count()

        
        return render(request,'dashboard.html',{'nt':notes,'search':search,'count':count})
    return redirect('users:sign-in')

def edit(request,id):
    


    if request.user.is_authenticated:
        note=Notes.objects.get(id=id)
        editForm=NotesForm(instance=note)
        notes=Notes.objects.all()
        if request.method=='POST':
            editForm=NotesForm(request.POST,instance=note)
            if editForm.is_valid():
                editForm.save()
                return redirect('notes:notes')
            
        return render(request,'edit.html',{'edit_form':editForm,'notes':notes})
    return redirect('users:sign-in')
    

def delete(request,id):
    if request.user.is_authenticated:
        Notes.objects.get(id=id).delete()

        return redirect('notes:notes')
    return redirect('users:sign-in')


