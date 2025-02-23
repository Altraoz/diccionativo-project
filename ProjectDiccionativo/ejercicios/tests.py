# accounts/tests.py
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

class SignUpPageTests(TestCase):
    def test_signup_page_status_code(self):
        response = self.client.get(reverse("signup"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "registration/signup.html")

    def test_signup_form(self):
        response = self.client.post(
            reverse("signup"),
            {
                "username": "nuevo_usuario",
                "email": "nuevo@example.com",
                "age": 20,
                "role": "estudiante",
                "password1": "testpass123",
                "password2": "testpass123",
            },
        )
        self.assertEqual(response.status_code, 302)
        user = get_user_model().objects.get(username="nuevo_usuario")
        self.assertEqual(user.email, "nuevo@example.com")
