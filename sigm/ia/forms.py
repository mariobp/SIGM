# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
import models

class CustomAuthenticationForm(AuthenticationForm):
    def confirm_login_allowed(self, user):
        if not user.is_active:
            raise forms.ValidationError('Se ha producido un problema con tu nombre de usuario.', code='invalid_login')
    # end def
# end class


class EstudianteForm(forms.ModelForm):

    class Meta:
        model = models.Estudiante
        exclude = ()
    # end class
# end class 
