from django import forms
from .models import Comment


# class CommentForm(forms.ModelForm):
#     class Meta:
#         model = Comment
#         fields = ['text']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
          'text': forms.Textarea(attrs={
                               'style': 'height: 200px;width:600px'}),
        }
