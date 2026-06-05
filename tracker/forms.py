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

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        for field in self.fields.values():

            field.widget.attrs.update({
                "class": "form-control"
            })