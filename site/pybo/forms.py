from django import forms
from pybo.models import world

class worldForm(forms.ModelForm):
    class Meta:
        model = world
        fields = ['CONTINENT', 'COUNTRY']
        labels = {
            'CONTINENT' : '대륙',
            'COUNTRY' : '나라이름',
        }
