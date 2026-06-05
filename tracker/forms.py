from django import forms
from .models import Application


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