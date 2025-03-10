from django import forms

PRODUCT_QUANTITY_CHOICE = [(i, str(i)) for i in range(1,21)]

class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(
        choices = PRODUCT_QUANTITY_CHOICE,
        coerce=int,
        initial=1,
        widget=forms.NumberInput(attrs={'class': 'form-control form-control-sm', 'min': '1', 'style':'width:60px; text-align:center;'})
    )
    override = forms.BooleanField(
        required = False,
        initial=False,
        widget= forms.HiddenInput
    )