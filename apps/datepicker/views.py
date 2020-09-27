from django.shortcuts import render
from . forms import DateForm

# Create your views here.

def home(request):
    form = DateForm
    return render(request, 'datepicker/index.html', context={'form': form})