from django.shortcuts import render

# Create your views here.
def home_page(request):
    t = request.GET.get('signIn', 'True') == 'True' 
    s = request.GET.get('signUp', 'False') == 'True'
    if request.user.is_authenticated:
        t = False
        s = False
    
    return render(request, 'home.html', {'signIn': t,'signUp':s})
