from django import forms

from .models import Auto


class AutoForm(forms.ModelForm):
    class Meta:
        model = Auto
        fields = ["marca", "modelo", "anio", "precio"]
        labels = {
            "marca": "Marca",
            "modelo": "Modelo",
            "anio": "Año",
            "precio": "Precio",
        }
        widgets = {
            "marca": forms.TextInput(attrs={"class": "form-control"}),
            "modelo": forms.TextInput(attrs={"class": "form-control"}),
            "anio": forms.NumberInput(attrs={"class": "form-control"}),
            "precio": forms.NumberInput(
                attrs={"class": "form-control", "step": "0.01"}
            ),
        }
