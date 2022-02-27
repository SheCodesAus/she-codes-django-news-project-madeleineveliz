from django import forms
from django.forms import ModelForm
from .models import NewsStory 

class StoryForm(ModelForm):
#     error_css_class = 'error-field'
#     required_css_class = 'required-field'

    title = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control",
    "placeholder": "Title"}))
    content = forms.CharField(widget=forms.Textarea(attrs={"placeholder":"Your amazing story goes here ♡"}))
    # image_url = forms.URLField(widget=forms.URLInput(attrs={'placeholder': "Image URL"}))
    # pub_date = forms.DateField(widget = forms.DateInput(format=('%m/%d/%Y'),attrs= {'id': 'date', 'class':'form-control','placeholder':'Select a date','type':'date'}),)
    

    class Meta:
        model = NewsStory
        fields = ['title','pub_date', 'content']
        # 'image_url']
        widgets = {
            'pub_date': forms.DateInput(format=('%m/%d/%Y'),
            attrs={'id':'date', 'class':'form-control','placeholder':'Select a date',
            'type':'date'}),}
    
