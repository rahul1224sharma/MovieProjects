from django.shortcuts import render
from MovieApp.forms import MoviesForm
from MovieApp.models import Movies
# Create your views here.
def index(request):
    return render(request,'MovieApp/index.html')

def addmovie(request):
    formsobj=MoviesForm()
    if request.method=='POST':
        formsobj=MoviesForm(request.POST)
        if formsobj.is_valid():
            formsobj.save(commit=True)
            return index(request)
    return render(request,'MovieApp/add.html',{'form1':formsobj})

def listsmovie(request):
    movieslists=Movies.objects.all().order_by('-ratings')
    return render(request,'MovieApp/lists.html',{'movieslists':movieslists})