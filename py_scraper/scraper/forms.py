from django import forms


class ScrapeForm(forms.Form):
    url = forms.URLField(label="Web URL")
