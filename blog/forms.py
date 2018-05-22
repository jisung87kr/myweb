from django import forms
from .models import *

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        # fields = '__all__'
        # exclude = ['create_date', 'published_date']
        fields = ('title', 'cate', 'text', 'upload_file')
        widgets = {
            'upload_file' : forms.ClearableFileInput(attrs={'multuple' : True})
        }
