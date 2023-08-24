from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('first_name', 'last_name', 'email', 'phone_number',
                  'street_address1', 'street_address2',
                  'town_or_city', 'postcode', 'country',
                  'county', 'comment',)

    def __init__(self, *args, **kwargs):

        # Add placeholders and classes, remove auto-generated
        # labels and set autofocus on first field

        super().__init__(*args, **kwargs)
        placeholders = {
            'first_name': 'first name',
            'last_name': 'last name',
            'email': 'email address',
            'phone_number': 'phone number',
            'postcode': 'postal code',
            'town_or_city': 'town or city',
            'street_address1': 'street address 1',
            'street_address2': 'street address 2',
            'county': 'county',
            'comment': 'additional information',
        }

        self.fields['first_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            # style in checkout.css
            self.fields[field].widget.attrs['class'] = (
                'stripe-style-input w-100 mb-1')
            self.fields[field].label = False
            self.fields['comment'].widget.attrs['style'] = (
                'min-height:3rem'
            )
