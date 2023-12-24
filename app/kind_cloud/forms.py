from django.forms import ModelForm
from .models import Kind

class KindForm(ModelForm):
    class Meta:
        model = Kind
        fields = ['text']
