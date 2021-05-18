from django import forms
from  WebApp.models import Team,Player,Matches,Statistics

class TeamForm(forms.ModelForm):
    class Meta:
        model=Team
        fields=["tname","logourl","state"]


class PlayerForm(forms.ModelForm):
    class Meta:
        model=Player
        fields='__all__'

class MatchesForm(forms.ModelForm):
    class Meta:
        model=Matches
        fields='__all__'

class StatisticsForm(forms.ModelForm):
    class Meta:
        model=Statistics
        fields='__all__'