from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):

    ROLE = (
        ('developer', 'Developer'),
        ('professional', 'Professional'),
        ('student', 'Student'),
        ('enthusiast', 'Enthusiast')
    )

    # Primary User Informatiion
    first_name = forms.CharField(max_length=30, required=True, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=True, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    # User's Secondary Information
    birth_date = forms.DateField(help_text='Required. Format: YYYY-MM-DD',required = True)
    role = forms.ChoiceField(choices = ROLE,required = True) 
    organization = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Organization'}),required = True)
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'birth_date', 'role', 'organization')

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'