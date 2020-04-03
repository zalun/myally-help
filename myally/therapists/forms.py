from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms


class ShortActivityForm(forms.Form):
    use_custom_control = True
    online = forms.BooleanField(
        label="Pomagam",
        required=False,
        help_text="Zaznaczasz gdy jesteś gotowa/y nieść pomoc.",
    )
    busy = forms.BooleanField(
        label="Rozmawiam",
        required=False,
        help_text="Zaznaczasz gdy rozpoczynasz rozmowę.",
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()


class ShortTherapistForm(forms.Form):
    phone_number = forms.CharField(
        label="numer telefonu", max_length=200, required=False
    )
    whatsapp = forms.BooleanField(label="WhatsApp", required=False)
    skype_id = forms.CharField(label="Skype", max_length=200, required=False)
    messenger_id = forms.CharField(
        label="Messenger (FB)", max_length=200, required=False
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()

        self.helper.form_method = "post"
        self.helper.add_input(Submit("submit", "Zapisz"))
