from django import forms 
from .models import Contact
from snowpenguin.django.recaptcha3.fields import ReCaptchaField


class ContactForm(forms.ModelForm):
    """Форма подписки по email"""
    captcha = ReCaptchaField()

    class Meta:
        model = Contact
        fields = ("email", "captcha")
        widgets = {
            "email" : forms.TextInput(attrs={"class" : "editContent", "placeholder" : 'Your Email ...'})
        }
        labels = {
            "email" : '',
        }
