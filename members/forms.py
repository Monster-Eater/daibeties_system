from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm 
from home.models import Profile


class ProfilePicForm(forms.ModelForm):
    profile_image = forms.ImageField(label = "Profile Picture")

    class Meta:
        model = Profile
        fields = ('profile_image', )

class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(widget= forms.EmailInput(attrs= {'class':'form-control'}))
    first_name = forms.CharField(max_length=30,widget= forms.TextInput(attrs= {'class':'form-control'}))
    last_name = forms.CharField(max_length=50,widget= forms.TextInput(attrs= {'class':'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email','password1', 'password2')

    
    def __init__(self, *arg, **kwargs):
        super(RegisterUserForm, self).__init__(*arg, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'