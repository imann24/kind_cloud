import os
import requests
from django.forms import CharField, ModelForm, Textarea
from django.core import validators
from .models import Kind


def make_request_to_sentiment_api(text):
    url = f'https://{os.environ.get("RAPID_API_HOST")}/analyze/'
    querystring = {'text': text}
    headers = {
	    'X-RapidAPI-Key': os.environ.get('RAPID_API_KEY'),
	    'X-RapidAPI-Host': os.environ.get('RAPID_API_HOST'),
    }
    response = requests.get(url, headers=headers, params=querystring)
    return response.json().get('type', False)

class KindForm(ModelForm):
    text = CharField(widget=Textarea(attrs={'rows': 3, 'cols': 40}))
    def __init__(self, *args, **kwargs):
        super(KindForm, self).__init__(*args, **kwargs)
        self.fields['text'].label = 'Kind Words'

    class Meta:
        model = Kind
        fields = ['text']

    def clean_text(self):
        text = self.cleaned_data.get('text', False)
        if text:
            if len(text) < 5:
                raise validators.ValidationError('Kind Words must be at least 5 characters long.')
            sentiment = make_request_to_sentiment_api(text)
            # allow through 'neutral' sentiments too
            if sentiment == 'negative':
                raise validators.ValidationError('Kind Words must be positive.')
            return text
