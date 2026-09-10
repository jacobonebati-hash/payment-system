from django import forms

from .models import Member, Payment


class MemberForm(forms.ModelForm):

    class Meta:

        model = Member

        fields = [
            "jina",
            "simu",
            "eneo",
            "kiasi_anachotakiwa",
        ]

        widgets = {

            "jina": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Jina kamili",
                }
            ),

            "simu": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "07XXXXXXXX",
                }
            ),

            "eneo": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Eneo/Kijiji",
                }
            ),

            "kiasi_anachotakiwa": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "min": "0",
                    "step": "100",
                }
            ),
        }


class PaymentForm(forms.ModelForm):

    class Meta:

        model = Payment

        fields = [
            "member",
            "kiasi",
            "payment_method",
            "transaction_number",
            "maelezo",
        ]

        widgets = {

            "member": forms.Select(
                attrs={
                    "class": "form-select"
                }
            ),

            "kiasi": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "min": "1",
                    "step": "100",
                }
            ),

            "payment_method": forms.Select(
                attrs={
                    "class": "form-select"
                }
            ),

            "transaction_number": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Transaction / Risiti",
                }
            ),

            "maelezo": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 3,
                }
            ),
        }

    def clean_kiasi(self):

        kiasi = self.cleaned_data["kiasi"]

        if kiasi <= 0:

            raise forms.ValidationError(
                "Kiasi lazima kiwe zaidi ya sifuri."
            )

        return kiasi


class ExcelImportForm(forms.Form):

    excel_file = forms.FileField(
        label="Chagua Excel",
        widget=forms.FileInput(
            attrs={
                "class": "form-control",
                "accept": ".xlsx",
            }
        )
    )

    kiasi_anachotakiwa = forms.DecimalField(
        label="Kiasi anachotakiwa kulipa",
        min_value=0,
        initial=10000,
        decimal_places=2,
        widget=forms.NumberInput(
            attrs={
                "class": "form-control",
                "step": "100",
            }
        )
    )

    def clean_excel_file(self):

        file = self.cleaned_data["excel_file"]

        if not file.name.lower().endswith(".xlsx"):

            raise forms.ValidationError(
                "Tafadhali tumia Excel ya .xlsx"
            )

        return file