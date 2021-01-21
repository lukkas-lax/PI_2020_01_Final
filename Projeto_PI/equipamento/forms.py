from django import forms  
from equipamento.models import Equipamento
from equipamento.models import EquipamentosFixos 
from equipamento.models import Alocacao 
from equipamento.models import Manutencao

class EquipamentoForm(forms.ModelForm):  
    class Meta:  
        model = Equipamento  
        fields = "__all__"  
        
class EquipamentosFixosForm(forms.ModelForm):  
    class Meta:  
        model = EquipamentosFixos  
        fields = "__all__"  
        
class AlocacaoForm(forms.ModelForm):  
    class Meta:  
        model = Alocacao  
        fields = "__all__" 
        
class ManutencaoForm(forms.ModelForm):  
    class Meta:  
        model = Manutencao  
        fields = "__all__" 