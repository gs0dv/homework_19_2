from django import forms

from catalog.models import Product


class ProductForm(forms.ModelForm):
    FORBIDDEN_WORDS = (
        'казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар')

    class Meta:
        model = Product
        fields = '__all__'

    def clean_product_name(self):
        cleaned_data = self.cleaned_data['product_name']

        if cleaned_data.lower() in self.FORBIDDEN_WORDS:
            raise forms.ValidationError('Название состоит из запрещенных слов!')
        return cleaned_data

    def clean_product_description(self):
        cleaned_data = self.cleaned_data['product_description']

        if cleaned_data.lower() in self.FORBIDDEN_WORDS:
            raise forms.ValidationError('Описание состоит из запрещенных слов!')
