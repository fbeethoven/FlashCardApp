from django import forms
from .models import flashCard

class CreateNewList(forms.Form):
    name = forms.CharField(label="Name",max_length=200)
    check = forms.BooleanField(required=False)


class CreateNewDeck(forms.Form):
    name = forms.CharField(label="Name",max_length=200)

class CreateflashCard(forms.Form):
    name = forms.CharField(label="Name", max_length=100, required = False)
    question = forms.CharField(label = "Question", max_length=200)
    answer = forms.CharField(
            label = "Answer",
            widget = forms.Textarea )
