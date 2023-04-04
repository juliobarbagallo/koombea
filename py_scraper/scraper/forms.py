from django import forms

class ScrapedPageForm(forms.Form):
    url = forms.URLField(label='Web URL')
