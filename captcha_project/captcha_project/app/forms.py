from django import forms
from captcha.fields import CaptchaField
class CaptchaForm(forms.Forms):
    captch=CaptchaField()