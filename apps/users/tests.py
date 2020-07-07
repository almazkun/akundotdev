from django.test import TestCase

from .models import CustomUser


# Create your tests here.
normal_user = {"username": "normal", "email": "normal@user.com", "password": "foo", "photo": "https://photo.com/photo.png"}

super_user = {"username": "super", "email": "super@user.com", "password": "foo", "photo": "https://photo.com/photo.png"}


class UsersManagersTests(TestCase):
    def test_create_user(self):
        test_object = normal_user
        CustomUser.objects.create_user(**test_object)
        obj = CustomUser.objects.get(username=test_object["username"])

        self.assertEqual(obj.username, test_object["username"])
        self.assertEqual(obj.email, test_object["email"])
        self.assertEqual(obj.photo, test_object["photo"])
        self.assertTrue(obj.is_active)
        self.assertFalse(obj.is_staff)
        self.assertFalse(obj.is_superuser)

    def test_create_superuser(self):
        test_object = super_user
        CustomUser.objects.create_superuser(**test_object)
        obj = CustomUser.objects.get(username=test_object["username"])

        self.assertEqual(obj.username, test_object["username"])
        self.assertEqual(obj.email, test_object["email"])
        self.assertEqual(obj.photo, test_object["photo"])
        self.assertTrue(obj.is_active)
        self.assertTrue(obj.is_staff)
        self.assertTrue(obj.is_superuser)
