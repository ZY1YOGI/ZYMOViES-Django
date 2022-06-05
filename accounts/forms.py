from django                     import forms
from .models                    import Profile
from django.contrib.auth.forms  import UserCreationForm
from django.contrib.auth.models import User








class CreateUserForm(UserCreationForm):
    username = forms.CharField(required=True, min_length=4, max_length=12, widget=forms.TextInput(attrs={'class':"input-field",
                                                                                                          'placeholder':"Username",
                                                                                                          'autofocus': False
                                                                                                            }))

    email    = forms.EmailField(required=True,min_length=10,max_length=24, widget=forms.EmailInput(attrs={'class':"input-field",
                                                                                                          'placeholder':"Email",}))

    password1= forms.CharField(required=True, min_length=8, max_length=30, widget=forms.PasswordInput(attrs={'class':"input-field",
                                                                                                             'placeholder':"Enter Password",}))

    password2= forms.CharField(required=True, min_length=8, max_length=30, widget=forms.PasswordInput(attrs={'class':"input-field",
                                                                                                             'placeholder':"Confrom Password",}))
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class Login_Form(forms.ModelForm):
    username = forms.CharField(required=True, min_length=4, max_length=12, widget=forms.TextInput(attrs={'class':"input-field",
                                                                                                        'placeholder':"Username",
                                                                                                        'autofocus': True}))
                                                                            
    password = forms.CharField(required=True, min_length=8, max_length=30, widget=forms.PasswordInput(attrs={'class':"input-field",
                                                                                                             'placeholder':"Enter Password",}))
    class Meta:
        model = User
        fields = ['username', 'password']

class UpdateUserForm(forms.ModelForm):
    username = forms.CharField()
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class UpdateProfileForm(forms.ModelForm):
    image = forms.ImageField()

    class Meta:
        model = Profile
        fields = ['image']