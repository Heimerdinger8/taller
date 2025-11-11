from django import forms
from .models import SparePart, Mechanic

class SparePartForm(forms.ModelForm):
    class Meta:
        model = SparePart
        fields = ['name', 'description', 'quantity', 'price', 'image']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

class MechanicForm(forms.ModelForm):
    class Meta:
        model = Mechanic
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
