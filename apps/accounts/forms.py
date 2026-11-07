"""Formularios del módulo de identidad y acceso."""

from django import forms
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm as DjangoPasswordChangeForm
from django.contrib.auth.hashers import check_password
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
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

    def clean_new_password1(self):
        """Valida con los validadores configurados y evita reutilizar la actual."""
        password1 = self.cleaned_data.get("new_password1")
        if password1 and self.user and self.user.check_password(password1):
            raise ValidationError(
                "La nueva contraseña no puede ser idéntica a la actual."
            )
        return password1


class NuevoPasswordForm(forms.Form):
    """Formulario de recuperación: frase de rescate + nueva contraseña.

    La nueva contraseña debe superar los validadores configurados de Django
    (mínimo 8 caracteres, no reutilización, similitud, etc.) y coincidir con su
    confirmación.
    """

    frase_rescate = forms.CharField(
        label="Frase de rescate",
        max_length=256,
        widget=forms.TextInput(attrs={"autocomplete": "off"}),
    )
    password1 = forms.CharField(
        label="Nueva contraseña",
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
    )
    password2 = forms.CharField(
        label="Confirmar nueva contraseña",
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
    )

    def __init__(self, usuario=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.usuario = usuario

    def clean_password1(self):
        password1 = self.cleaned_data.get("password1")
        if password1:
            try:
                validate_password(password1, self.usuario)
            except ValidationError as exc:
                for error in exc.messages:
                    self.add_error("password1", error)
        return password1

    def clean_password2(self):
        password2 = self.cleaned_data.get("password2")
        if password2 and password2 != self.cleaned_data.get("password1"):
            self.add_error("password2", "Las contraseñas no coinciden.")
        return password2

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")
        if password1 and password2 and password1 == password2:
            if self.usuario and check_password(password1, self.usuario.password):
                self.add_error(
                    "password1",
                    "La nueva contraseña no puede ser idéntica a la actual.",
                )
        return cleaned_data
