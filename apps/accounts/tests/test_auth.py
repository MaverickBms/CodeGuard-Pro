"""Pruebas del módulo accounts (identidad y acceso)."""

from django.test import TestCase
from django.contrib.auth import get_user_model
from django.utils import timezone

from apps.accounts.services import (
    crear_usuario_inicial,
    generar_frase_rescate,
    validar_frase_rescate,
    autenticar_usuario,
)


class ServiciosIdentidadTests(TestCase):
    def test_generar_frase_rescate_longitud(self):
        """La frase de rescate debe tener la longitud solicitada."""
        frase = generar_frase_rescate(32)
        self.assertEqual(len(frase), 32)

    def test_crear_usuario_inicial_devuelve_usuario_y_frase(self):
        """crear_usuario_inicial devuelve el usuario y la frase de rescate."""
        User = get_user_model()
        self.assertFalse(User.objects.exists())

        usuario, frase = crear_usuario_inicial(
            "nuevousuario", "Pass1234!", email="nuevo@test.local"
        )
        self.assertIsNotNone(usuario)
        self.assertEqual(usuario.username, "nuevousuario")
        self.assertTrue(isinstance(frase, str) and len(frase) >= 32)
        self.assertTrue(User.objects.filter(username="nuevousuario").exists())

    def test_crear_usuario_inicial_duplicado_falla(self):
        """No se puede crear un segundo usuario inicial."""
        User = get_user_model()
        User.objects.create_superuser("dupe", "dupe@test.local", "Pass1234!")
        with self.assertRaises(RuntimeError):
            crear_usuario_inicial("dupe2", "Pass1234!")

    def test_validar_frase_rescate_un_solo_uso(self):
        """La frase de rescate es válida una sola vez."""
        User = get_user_model()
        usuario, frase_texto = crear_usuario_inicial(
            "rescateuser", "Pass1234!", email="rescate@test.local"
        )

        self.assertTrue(validar_frase_rescate(usuario, frase_texto))
        self.assertFalse(validar_frase_rescate(usuario, frase_texto))

    def test_autenticar_usuario_credenciales_validas(self):
        """autenticar_usuario devuelve el usuario con credenciales válidas."""
        User = get_user_model()
        usuario, _ = crear_usuario_inicial(
            "authuser", "Pass1234!", email="auth@test.local"
        )
        resultado = autenticar_usuario("authuser", "Pass1234!")
        self.assertIsNotNone(resultado)
        self.assertEqual(resultado.username, "authuser")

    def test_autenticar_usuario_credenciales_invalidas(self):
        """autenticar_usuario devuelve None con credenciales inválidas."""
        User = get_user_model()
        crear_usuario_inicial("authuser2", "Pass1234!", email="auth2@test.local")
        resultado = autenticar_usuario("authuser2", "contraseña_mala")
        self.assertIsNone(resultado)
