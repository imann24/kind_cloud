from django.forms import ModelForm
from .models import Kind

class KindForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(KindForm, self).__init__(*args, **kwargs)
        self.fields['text'].label = "Kind Words"

    class Meta:
        model = Kind
        fields = ['text']
