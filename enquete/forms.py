from django import forms
from .models import Enquete, Delegation, Localite

class EnqueteForm(forms.ModelForm):
    typeBiomasse = forms.MultipleChoiceField(
        choices=Enquete.typeBiomasse_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        required=True,
        label="Quels types de biomasse utilisez-vous pour vos besoins énergétiques ?"
    )
  
    usageBiomasse = forms.MultipleChoiceField(
        choices=Enquete.usageBiomasse_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        required=True,
        label="Pour quels usages principaux utilisez-vous la biomasse ?"
    )

    sourceApprov = forms.MultipleChoiceField(
        choices=Enquete.sourceApprov_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        required=True,
        label="Quelle est votre principale source d'approvisionnement en biomasse ?"
    )

    raisonUsage = forms.MultipleChoiceField(
        choices=Enquete.raisonUsage_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        required=True,
        label="Pourquoi utilisez-vous principalement la biomasse ?"
    )

    sourceAlter = forms.MultipleChoiceField(
        choices=Enquete.sourceAlter_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        required=True,
        label="Quelles autres sources d'énergie utilisez-vous ou envisagez-vous d'utiliser ?"
    )
    
    delegation = forms.ModelChoiceField(
        queryset=Delegation.objects.none(),  # We will populate this in the form initialization
        required=True,
        label="Délégation"
    )
    
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)  # Get the agent from the view
        super().__init__(*args, **kwargs)
        
        if user:
            print("user's gouvernorat:", user.gouvernorat)
            self.instance.user = user

            # Filter the delegations based on the agent's gouvernorat
            self.fields['delegation'].queryset = Delegation.objects.filter(gouvernorat=user.gouvernorat)
        
        # Initially empty localite field; it will be populated dynamically based on the selected delegation
        self.fields['localite'].queryset = Localite.objects.none()
        
        if 'delegation' in self.data:
            try:
                delegation_id = int(self.data.get('delegation'))
                self.fields['localite'].queryset = Localite.objects.filter(delegation_id=delegation_id).order_by('libelle')
            except (ValueError, TypeError):
                pass  # Invalid input; ignore and return empty queryset
        
        self.order_fields(['delegation'] + list(self.fields.keys()))


    def clean_QteBoisChauffage(self):
        data = self.cleaned_data.get('QteBoisChauffage')
        if data < 0:
            raise forms.ValidationError("La quantité de bois de chauffage doit être positive.")
        return data

    def clean_QteResiduAgric(self):
        data = self.cleaned_data.get('QteResiduAgric')
        if data < 0:
            raise forms.ValidationError("La quantité de résidus agricoles doit être positive.")
        return data

    def clean_QteDechetsVeget(self):
        data = self.cleaned_data.get('QteDechetsVeget')
        if data < 0:
            raise forms.ValidationError("La quantité de déchets végétaux doit être positive.")
        return data

    def clean_QteCharbonBois(self):
        data = self.cleaned_data.get('QteCharbonBois')
        if data < 0:
            raise forms.ValidationError("La quantité de charbon de bois doit être positive.")
        return data

    class Meta:
        model = Enquete
        exclude = ['user']
        widgets = {
            'longitude': forms.HiddenInput(),
            'latitude': forms.HiddenInput(),
        }
