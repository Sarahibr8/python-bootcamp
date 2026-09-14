from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
    rating = forms.IntegerField(required=False)

    def clean_message(self):
        message = self.cleaned_data["message"]

        if len(message) < 20:
            raise forms.ValidationError("Message is too short.")

        return message