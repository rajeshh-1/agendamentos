from django import forms
from app.models import ContactGroup,Contact

# Create the form class.
class ContactGroupForm (forms.ModelForm):
    class Meta:
        model = ContactGroup
        fields = ['description']
        widgets = {
            'description': forms.TextInput(attrs={'class': 'form-control'}),
        }


class MenuModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return "%s) %s" % (obj.id,obj.description)

class ContactForm(forms.ModelForm):
    
    contactGroup = MenuModelChoiceField(queryset = ContactGroup.objects.all())
    
    class Meta:
        model = Contact
        fields = ['name', 'phone', 'email','address', 'number', 'district', 'cep', 'city', 'state' ,'contactGroup']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'number': forms.TextInput(attrs={'class': 'form-control'}),
            'district': forms.TextInput(attrs={'class': 'form-control'}),
            'cep': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'state': forms.TextInput(attrs={'class': 'form-control'}),
            'contactGroup': forms.Select(attrs={'class': 'form-select'}),
        }