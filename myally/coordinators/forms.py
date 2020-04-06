from crispy_forms.bootstrap import FieldWithButtons, StrictButton
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from django import forms


class InviteCoordinatorForm(forms.Form):
    email = forms.EmailField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = "form-horizontal"
        self.helper.field_template = "bootstrap4/layout/inline_field.html"
        self.helper.layout = Layout(
            "email",
            FieldWithButtons(
                "email", StrictButton("Invite Coordinator", css_class="btn-primary")
            ),
        )
