from django import forms

# Create your forms here
class CommentForm(forms.Form):
    author = forms.CharField(
        max_length = 60,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Your name",
            
        })
    
    )

    email = forms.CharField(
        max_length = 60,
        widget=forms.TextInput(attrs={
            "class": "EmailInput",
            "placeholder": "Your email"
        })
    )

    phone = forms.CharField(
        max_length = 60,
        widget=forms.TextInput(attrs={
            "class": "PhoneNumber",
            "placeholder": "Your phone"
        })
    )

    body = forms.CharField(
        widget = forms.Textarea(attrs={
            "class": "form-control",
            "placeholder": "Leave your comment"
        })
    )