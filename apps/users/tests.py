from django.test import TestCase

from .models import CustomUser


# Create your tests here.
normal_user = {"username": "normal", "email": "normal@user.com", "password": "foo"}

super_user = {"username": "super", "email": "super@user.com", "password": "foo"}


class UsersManagersTests(TestCase):
    def test_create_user(self):
        CustomUser.objects.create_user(**normal_user)
        obj = CustomUser.objects.get(username=normal_user["username"])

        self.assertEqual(obj.username, normal_user["username"])
        self.assertEqual(obj.email, normal_user["email"])
        self.assertTrue(obj.is_active)
        self.assertFalse(obj.is_staff)
        self.assertFalse(obj.is_superuser)

    def test_create_superuser(self):
        CustomUser.objects.create_superuser(**super_user)
        obj = CustomUser.objects.get(username=super_user["username"])

        self.assertEqual(obj.username, super_user["username"])
        self.assertEqual(obj.email, super_user["email"])
        self.assertTrue(obj.is_active)
        self.assertTrue(obj.is_staff)
        self.assertTrue(obj.is_superuser)
