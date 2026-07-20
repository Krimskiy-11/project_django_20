from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    phone_number = forms.CharField(max_length=15, required=False, help_text='Необязательное поле. Введите ваш номер телефона.')
    country = forms.CharField(max_length=35, required=False, help_text='Необязательное поле. Укажите вашу страну.')
    usable_password = None

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('email', 'username', 'first_name', 'last_name', 'phone_number', 'country', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)

        self.fields["email"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Электронная почта"}
        )

        self.fields["username"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Никнейм"}
        )

        self.fields["first_name"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Имя"}
        )

        self.fields["last_name"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Фамилия"}
        )

        self.fields["phone_number"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Номер телефона"}
        )

        self.fields["country"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Страна"}
        )

        self.fields["password1"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Пароль"}
        )

        self.fields["password2"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Повторите пароль"}
        )


    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if phone_number and not phone_number.isdigit():
            raise forms.ValidationError('Phone number must contain only digits.')
        return phone_number

    def clean_country(self):
        country = self.cleaned_data.get('country')
        if country and not country.isalpha():
            raise forms.ValidationError('Country must contain only alphabetic characters.')
        return country
