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
            "interview_date",
            "interview_time",
            "notes",
        ]

        widgets = {

            "applied_date":
                forms.DateInput(
                    attrs={
                        "type": "date"
                    }
                ),
            "interview_date": forms.DateInput(
                attrs={
                    "type": "date",
                    "class": "form-control"
                }
            ),

            "interview_time": forms.TimeInput(
                attrs={
                    "type": "time",
                    "class": "form-control"
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
    def clean(self):

        cleaned_data = super().clean()

        status = cleaned_data.get("status")

        interview_date = cleaned_data.get(
            "interview_date"
        )

        if status == "Interview" and not interview_date:

            raise forms.ValidationError(
                "Interview date is required when status is Interview."
            )

        return cleaned_data

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