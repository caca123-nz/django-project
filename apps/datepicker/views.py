from django.shortcuts import render
from . forms import DateForm, DatePickerForm

# Create your views here.

def home(request):
    form = DateForm
    form_picker = DatePickerForm
    return render(request, 'datepicker/index.html', context={'form': form, 'form_picker': form_picker})