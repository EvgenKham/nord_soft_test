from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password


class Profile(models.Model):
    email = models.EmailField(unique=True, blank=False)
    first_name = models.CharField(max_length=256, blank=False)
    last_name = models.CharField(max_length=256, blank=False)
    password = models.CharField(max_length=128)
    number_phone = models.CharField(max_length=128, blank=False)
    city = models.CharField(max_length=128, blank=True, default="0000000")
    address = models.CharField(max_length=256, blank=True, default="0000000")

    class Meta:
        ordering = ['id', 'email', 'first_name', 'last_name']
        index_together = [
            ['id', 'email']
        ]
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

    def __str__(self):
        return self.first_name

    def get_absolute_url(self):
        return reverse('user:detail', kwargs={'user': self.first_name})

    def generation_password(self):
        self.password = User.objects.make_random_password()

        # self.password = make_password(password)
        return self.password

    # def check_password(self, password):
    #     return check_password(self.password, password)


