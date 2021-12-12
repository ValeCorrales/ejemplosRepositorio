from django import forms

class EstadioFormulario(forms.Form):
    
    #especificar campos
    direccion = forms.CharField()
    anioFund = forms.IntegerField()