from django import forms
from ..models.comment import Comment


class CommentForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['comment'].widget.attrs.update({'class': 'form-control bg-dark text-white-50 mt-2', 'placeholder':'What are your thoughts?'})
        self.fields['parent'].widget = forms.HiddenInput()
    
    class Meta:
        model = Comment
        fields = ['comment', 'parent']
