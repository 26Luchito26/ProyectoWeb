from django import forms
from .models import Solicitudes_Epps, Solicitudes_Retiro, Solicitudes_Material

class SolicitudEppsForm(forms.ModelForm):
    class Meta:
        model = Solicitudes_Epps
        fields = ['nombreEpps', 'fecha_realizarEP', 'descripcionEpps', 'estadoEpps', 'tipo_materialEpps']
        widgets = {
            'fecha_realizarEP': forms.DateInput(attrs={'type': 'date'})
        }
class SolicitudRetiroForm(forms.ModelForm):
    class Meta:
        model = Solicitudes_Retiro
        fields = ['nombre_retiro', 'fecha_realizarR', 'descripcionRetiro', 'cantidadRetiro', 'estadoRetiro', 'tipo_materialRetiro']
        widgets = {
            'fecha_realizarR': forms.DateInput(attrs={'type': 'date'})
        }
class SolicitudMaterialForm(forms.ModelForm):
    class Meta:
        model = Solicitudes_Material
        fields = ['nombre_material', 'tipo_material', 'fecha_realizarM', 'descripcionMaterial', 'cantidadMaterial', 'estadoMaterial']
        widgets = {
            'fecha_realizarM': forms.DateInput(attrs={'type': 'date'})
        }