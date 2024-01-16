from django import forms
from .models import (
    Institute,
    SubjectTopic,
    Keyword,
    ThesisType,
    Language,
    Thesis,
)


class ThesisCreationForm(forms.ModelForm):

    class Meta:
        model = Thesis
        fields = [
            'title',
            'abstract',
            'text',
            'thesis_type',
            'topic',
            'keywords',
            'institute',
            'language',
            'page_amount',
            'year',
        ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control w-100'}),
            'abstract': forms.Textarea(attrs={'class': 'form-control w-100'}),
            'text': forms.Textarea(attrs={'class': 'form-control w-100'}),
            'thesis_type': forms.Select(attrs={'class': 'form-select w-100'}),
            'topic': forms.Select(attrs={'class': 'form-select w-100'}),
            'keywords': forms.SelectMultiple(attrs={'class': 'form-select w-100'}),
            'institute': forms.Select(attrs={'class': 'form-select w-100'}),
            'language': forms.Select(attrs={'class': 'form-select w-100'}),
            'page_amount': forms.NumberInput(attrs={'class': 'form-control w-100'}),
            'year': forms.NumberInput(attrs={'class': 'form-control w-100'}),
        }

# title = forms.CharField(
#     label='Title',
#     max_length=500,
#     widget=forms.TextInput(attrs={'class': 'form-control'}
# ))
# abstract = forms.CharField(
#     label='Abstract',
#     widget=forms.Textarea(attrs={'class': 'form-control'})
# )
# text = forms.CharField(
#     label='Text',
#     widget=forms.Textarea(attrs={'class': 'form-control'})
# )
# thesis_type = forms.ModelChoiceField(
#     queryset=ThesisType.objects.all(),
#     widget=forms.Select(attrs={'class': 'form-control'})
# )
# topic = forms.ModelChoiceField(
#     queryset=SubjectTopic.objects.all(),
#     widget=forms.Select(attrs={'class': 'form-control'})
# )
# keywords = forms.ModelMultipleChoiceField(
#     queryset=Keyword.objects.all(),
#     widget=forms.SelectMultiple(attrs={'class': 'form-control'})
# )
# institute = forms.ChoiceField(
#     choices=[(institute.id, institute.name) for institute in Institute.objects.all()],
#     widget=forms.Select(attrs={'class': 'form-control'})
# )
# language = forms.ModelChoiceField(
#     queryset=Language.objects.all(),
#     widget=forms.Select(attrs={'class': 'form-control'})
# )
# page_amount = forms.IntegerField(
#     widget=forms.NumberInput(attrs={'class': 'form-control'})
# )
# year = forms.IntegerField(
#     widget=forms.NumberInput(attrs={'class': 'form-control'})
# )