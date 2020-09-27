from django import forms
from .widgets import BootstrapDateTimePickerInput

class DateForm(forms.Form):
    _form = forms.DateTimeField(
        input_formats=['%d/%m/%Y'], 
        widget=BootstrapDateTimePickerInput()
    )
    _to = forms.DateTimeField(
        input_formats=['%d/%m/%Y'], 
        widget=BootstrapDateTimePickerInput()
    )