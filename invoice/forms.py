from django import forms
from django.contrib.auth import get_user_model
from addressbook.models import Address
from invoice.models import Invoice


class InvoiceAdminForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        try:
            address = args[0]['address']
        except IndexError:
            address = None

        try:
            user = args[0]['user']
            if not address and user:
                address_pk = get_user_model().objects.get(pk=user).address.pk
                args[0]['address'] = address_pk
        except (IndexError, Address.DoesNotExist):
            pass

        self.fields = ('user', 'address', 'invoice_date', 'paid_date', 'draft', 'currency')
        super(InvoiceAdminForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Invoice
