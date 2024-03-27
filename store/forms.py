from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from store.models import Artist, Painting


class UpdateArtistForm(UserChangeForm):
    password = None
    #email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}))
    #first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}))
    #last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}))

    class Meta:
        model = Artist
        fields = ('bio', 'web_url', 'inst_url', 'fcbk_url', 'x_url', 'image')

    def __init__(self, *args, **kwargs):
        super(UpdateArtistForm, self).__init__(*args, **kwargs)

        self.fields['bio'].widget.attrs['class'] = 'form-control'
        self.fields['bio'].widget.attrs['placeholder'] = 'Bio'
        self.fields['bio'].label = ''
        self.fields['bio'].help_text = '<span class="form-text text-muted"><small>Not required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

        self.fields['web_url'].widget.attrs['class'] = 'form-control'
        self.fields['web_url'].widget.attrs['placeholder'] = 'URL Web'
        self.fields['web_url'].label = ''

        self.fields['inst_url'].widget.attrs['class'] = 'form-control'
        self.fields['inst_url'].widget.attrs['placeholder'] = 'URL Instagram'
        self.fields['inst_url'].label = ''

        self.fields['fcbk_url'].widget.attrs['class'] = 'form-control'
        self.fields['fcbk_url'].widget.attrs['placeholder'] = 'URL Facebook'
        self.fields['fcbk_url'].label = ''

        self.fields['x_url'].widget.attrs['class'] = 'form-control'
        self.fields['x_url'].widget.attrs['placeholder'] = 'URL X'
        self.fields['x_url'].label = ''


class PaintingForm(ModelForm):

    class Meta:
        model = Painting
        # fields = "__all__"
        fields = ('name', 'description', 'support', 'technique', 'pheight', 'pwidth', 'category', 'price', 'available', 'image')

    def __init__(self, *args, **kwargs):
        super(PaintingForm, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['name'].widget.attrs['placeholder'] = 'name'
        self.fields['name'].label = 'Nombre'
        self.fields['name'].help_text = '<span class="form-text"></span>'

        self.fields['description'].widget.attrs['class'] = 'form-control'
        self.fields['description'].widget.attrs['placeholder'] = 'descripcion'
        self.fields['description'].label = 'Descripción'

        self.fields['support'].widget.attrs['class'] = 'form-select'
        self.fields['support'].label = 'Soporte'

        self.fields['technique'].widget.attrs['class'] = 'form-select'
        self.fields['technique'].label = 'Técnica'

        self.fields['pheight'].widget.attrs['class'] = 'form-control'
        self.fields['pheight'].label = 'Alto'

        self.fields['pwidth'].widget.attrs['class'] = 'form-control'
        self.fields['pwidth'].label = 'Ancho'

        self.fields['category'].widget.attrs['class'] = 'form-control'
        self.fields['category'].label = 'Categoría'

        self.fields['price'].widget.attrs['class'] = 'form-control'
        self.fields['price'].label = 'Precio'

        self.fields['available'].widget.attrs['class'] = 'form-check-input'
        self.fields['available'].label = 'Disponible'

        self.fields['image'].widget.attrs['class'] = 'form-control'
        self.fields['image'].label = 'Imagen'


class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}))
    first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}))
    last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'
