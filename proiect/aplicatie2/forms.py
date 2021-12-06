from django import forms

from aplicatie2.models import Companies


class CompaniesForm(forms.ModelForm):
    class Meta:
        model = Companies
        fields = '__all__'

    def __init__(self, pk, *args, **kwargs):
        super(CompaniesForm, self).__init__(*args, **kwargs)
        self.company_pk = pk

    def clean(self):
        cleaned_data = self.cleaned_data
        name_value = cleaned_data.get('name')
        if self.company_pk:
            if Companies.objects.filter(name=name_value).exclude(id=self.company_pk).exists():
                self._errors['name'] = self.error_class(["Numele deja exista"])
        else:
            if Companies.objects.filter(name=name_value).exists():
                self._errors['name'] = self.error_class(["Numele deja exista"])
        return cleaned_data
