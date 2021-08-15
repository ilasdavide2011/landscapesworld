from django.shortcuts import render
from .models import landscape

# Create your views here.
def home(request):
    landscapes = landscape.objects.all()
    return render(request, 'landscapes/home.html', {'landscapes': landscapes})
