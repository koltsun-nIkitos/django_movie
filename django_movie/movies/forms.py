from django import forms
from snowpenguin.django.recaptcha3.fields import ReCaptchaField

from .models import RattingStar, Reviews, Ratting


class ReviewsForm(forms.ModelForm):
    """Форма отзывов"""
    captcha = ReCaptchaField()

    class Meta:
        model = Reviews
        fields = ("name", "email", "text", "captcha")
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control border"}),
            "email": forms.EmailInput(attrs={"class": "form-control border"}),
            "text": forms.Textarea(attrs={"class": "form-control border"})
        }
class RattingForm(forms.ModelForm):
    """Форма добавления рейтинга"""
    star = forms.ModelChoiceField(
        queryset=RattingStar.objects.all(), widget=forms.RadioSelect(), empty_label=None
    )

    class Meta:
        model = Ratting
        fields = ("star",)