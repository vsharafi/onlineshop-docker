from django import forms


class AddProductToCartForm(forms.Form):
    QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 30)]
    quantity = forms.TypedChoiceField(choices=QUANTITY_CHOICES, coerce=int)
    # quantity = forms.NumberInput(attrs={'class': 'quantity-input', 'value': 1, 'min': 1})