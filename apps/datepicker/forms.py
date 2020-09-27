from django import forms
from .widgets import BootstrapDateTimePickerInput
from bootstrap_datepicker_plus import DatePickerInput
from .models import DatePicker

class DateForm(forms.Form):
    _form = forms.DateTimeField(
        input_formats=['%d/%m/%Y'], 
        widget=BootstrapDateTimePickerInput()
    )
    _to = forms.DateTimeField(
        input_formats=['%d/%m/%Y'], 
        widget=BootstrapDateTimePickerInput()
    )

class DatePickerForm(forms.ModelForm):
    class Meta:
        model = DatePicker
        fields = ['_from', '_to']
        widgets = {
            '_from': DatePickerInput(), # default date-format %m/%d/%Y will be used
            '_to': DatePickerInput(format='%Y-%m-%d'), # specify date-format
        }