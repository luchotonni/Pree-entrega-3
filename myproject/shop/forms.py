from django import forms
from .models import Cartera, Remera, Pulsera


class CarteraForm(forms.ModelForm):
    class Meta:
        model = Cartera
        fields = '__all__'


class RemeraForm(forms.ModelForm):
    class Meta:
        model = Remera
        fields = '__all__'


class PulseraForm(forms.ModelForm):
    class Meta:
        model = Pulsera
        fields = '__all__'


class CarteraSearchForm(forms.Form):
    nombre = forms.CharField(max_length=100, required=False)


class RemeraSearchForm(forms.Form):
    nombre = forms.CharField(max_length=100, required=False)


class PulseraSearchForm(forms.Form):
    nombre = forms.CharField(max_length=100, required=False)
