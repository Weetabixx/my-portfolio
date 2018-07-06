from django import forms

class PostForm(forms.Form):
    post_type = forms.CharField(max_length=100)
    post_title = forms.CharField(max_length=100)
    post_content = forms.CharField(widget=forms.Textarea)
    post_description = forms.CharField(max_length=100)
    post_confirm = forms.BooleanField(required=False)