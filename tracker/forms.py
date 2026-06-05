from django import forms
from .models import Application
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

class ApplicationForm(forms.ModelForm):

    class Meta:

        model = Application

        fields = [
            "company",
            "position",
            "location",
            "salary",
            "source",
            "status",
            "applied_date",
            "notes",
        ]

        widgets = {

            "applied_date":
                forms.DateInput(
                    attrs={
                        "type": "date"
                    }
                ),

            "notes":
                forms.Textarea(
                    attrs={
                        "rows": 4
                    }
                )
        }

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        for field in self.fields.values():

            field.widget.attrs.update({
                "class": "form-control"
            })

class RegisterForm(UserCreationForm):

    class Meta:

        model = User

        fields = [
            'username',
            'password1',
            'password2'
        ]

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        for field in self.fields.values():

            field.help_text = ""

            field.widget.attrs.update({

                'class': 'form-control bg-dark text-light border-secondary'

            })

class LoginForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        for field in self.fields.values():

            field.widget.attrs.update({

                'class': 'form-control bg-dark text-light border-secondary'

            })