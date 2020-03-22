from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms

class ShortTherapistForm(forms.Form):
    online = forms.BooleanField(label="online", required=False)
    busy = forms.BooleanField(label="busy", required=False)
    phone_number = forms.CharField(label="phone number", max_length=200, required=False)
    whatsapp = forms.BooleanField(label="WhatsApp", required=False)
    skype_id = forms.CharField(label="Skype", max_length=200, required=False)
    messenger_id = forms.CharField(label="Messenger (FB)", max_length=200, required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.add_input(Submit("submit", "Zapisz"))
