from django import forms

from catalog.models import Product, Version


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            if field_name == 'is_published':
                field.widget.attrs['class'] = 'form-check'


class ProductForm(StyleFormMixin, forms.ModelForm):
    FORBIDDEN_WORDS = (
        'казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар')

    class Meta:
        model = Product
        # fields = '__all__'
        exclude = ('owner',)

    def clean_product_name(self):
        cleaned_data = self.cleaned_data['product_name']

        if cleaned_data.lower() in self.FORBIDDEN_WORDS:
            raise forms.ValidationError('Название состоит из запрещенных слов!')
        return cleaned_data

    def clean_product_description(self):
        cleaned_data = self.cleaned_data['product_description']

        if cleaned_data.lower() in self.FORBIDDEN_WORDS:
            raise forms.ValidationError('Описание состоит из запрещенных слов!')
        return cleaned_data


class VersionForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Version
        exclude = ('is_current_version',)
