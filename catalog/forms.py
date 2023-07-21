from django.forms import ModelForm
from .models import tarea
class formularioTarea(ModelForm):
    class Meta:
        model = tarea
        fields = ["Nombre", "Descripción", "Importante"]
        