from django.contrib.auth.models import AbstractUser
from django.db import models, transaction


class CustomUser(AbstractUser):
    photo = models.CharField(verbose_name="Photo", max_length=255)
    github_link = models.CharField(verbose_name="Github", max_length=255, blank=True)
    linkedin_link = models.CharField(verbose_name="LinkedIn", max_length=255, blank=True)
    cv_link = models.CharField(verbose_name="Resume (CV)", max_length=255, blank=True)
    public_email = models.CharField(verbose_name="Email", max_length=255, blank=True)
    public_email = models.BooleanField(verbose_name="Main User", default=False)

    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        if not self.main_user:
            return super(CustomUser, self).save(*args, **kwargs)
        with transaction.atomic():
            CustomUser.objects.filter(
                main_user=True).update(main_user=False)
            return super(CustomUser, self).save(*args, **kwargs)