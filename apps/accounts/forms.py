"""Formularios del módulo de identidad y acceso."""

from django import forms
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm as DjangoPasswordChangeForm
from django.contrib.auth.models import AbstractUser


class LoginForm(AuthenticationForm):
    """Formulario de inicio de sesión con contraseña maestra."""

    username = forms.CharField(
        label="Usuario",
        max_length=150,
        widget=forms.TextInput(attrs={"autofocus": True, "autocomplete": "username"}),
    )
    password = forms.CharField(
        label="Contraseña maestra",
        widget=forms.PasswordInput(attrs={"autocomplete": "current-password"}),
    )

    def confirm_login_allowed(self, user: AbstractUser) -> None:
        if not user.is_active:
            raise forms.ValidationError(
                "Esta cuenta está inactiva.", code="inactive"
            )


class SetupInicialForm(forms.Form):
    """Formulario de configuración inicial: usuario, contraseña y aceptación de términos."""

    username = forms.CharField(
        label="Usuario",
        max_length=150,
        widget=forms.TextInput(attrs={"autocomplete": "username"}),
    )
    password1 = forms.CharField(
        label="Contraseña maestra",
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
    )
    password2 = forms.CharField(
        label="Confirmar contraseña maestra",
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
    )
    aceptar_terminos = forms.BooleanField(
        label="Acepto los términos de uso y el código de ética (RF-122)",
        required=True,
    )

    def clean_username(self):
        username = self.cleaned_data["username"]
        from apps.accounts.models import Usuario

        if Usuario.objects.filter(username=username).exists():
            raise forms.ValidationError("Este usuario ya existe.")
        return username

    def clean(self):
        cleaned = super().clean()
        p1 = cleaned.get("password1")
        p2 = cleaned.get("password2")
        if p1 and p2 and p1 != p2:
            raise forms.ValidationError("Las contraseñas no coinciden.")
        if p1 and len(p1) < 8:
            self.add_error(
                "password1",
                forms.ValidationError("La contraseña debe tener al menos 8 caracteres."),
            )
        return cleaned


class CambiarContraseñaForm(DjangoPasswordChangeForm):
    """Formulario para cambiar la contraseña maestra (Argon2)."""

    old_password = forms.CharField(
        label="Contraseña actual",
        widget=forms.PasswordInput(attrs={"autocomplete": "current-password"}),
    )
    new_password1 = forms.CharField(
        label="Nueva contraseña",
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
    )
    new_password2 = forms.CharField(
        label="Confirmar nueva contraseña",
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
    )
