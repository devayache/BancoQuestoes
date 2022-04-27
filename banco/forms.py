from django.forms import ModelForm
from banco.models import Questoes

class QuestoesForm(ModelForm):
    class Meta:
        model = Questoes
        fields =('__all__')