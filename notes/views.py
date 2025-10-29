from django.shortcuts import render,redirect
from django.http import HttpResponse
from notes.models import Notes
from notes.forms import NotesForm
from django.urls import reverse

# Create your views here.
def dashboard(request):
    if request.user.is_authenticated:
        
        if request.method=='POST':
            title=request.POST.get('title')
            note=request.POST.get('description')
            Notes.objects.create(user=request.user,title=title,note=note)
            return redirect('notes:notes')
            
        search=request.GET.get('search')
        notes=Notes.objects.filter(user=request.user)
        count=notes.count()
        if search:
            notes=Notes.objects.filter(user=request.user,title__icontains=search)
            count=notes.count()

        
        return render(request,'dashboard.html',{'nt':notes,'search':search,'count':count})
    
    url=reverse('home:guest-page')
    return redirect(f"{url}?signIn=True")

def edit(request,id): 
    if request.user.is_authenticated:
        print('achi======')
        note=Notes.objects.get(id=id)
        editForm=NotesForm(instance=note)
        notes=Notes.objects.filter(user=request.user)
        if request.method=='POST':
            print('vito88888888888')
            editForm=NotesForm(request.POST,instance=note)
            if editForm.is_valid():
                print('***************************')
                editForm.save()
                return redirect('notes:notes')
            
        return render(request,'edit.html',{'edit_form':editForm,'notes':notes})
    url=reverse('home:guest-page')
    return redirect(f"{url}?signIn=True")
    

def delete(request,id):
    if request.user.is_authenticated:
        Notes.objects.get(id=id).delete()

        return redirect('notes:notes')
    url=reverse('home:guest-page')
    return redirect(f"{url}?signIn=True")


