from django.db import models
from django.conf import settings
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from blog.managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    SUPERADMIN, USER = range(1, 3)

    ROLE_TYPES = (
        (SUPERADMIN, "Суперпользователь"),
        (USER, "Пользователь"),
    )

    objects = UserManager()

    id = models.AutoField(primary_key=True)
    username = models.CharField("Логин", max_length=50, default="", unique=True)
    first_name = models.CharField(
        "ФИО", max_length=100, default="", blank=True, null=True
    )
    email = models.EmailField("Почта", default="email@mail.com", blank=True, null=True)
    role = models.IntegerField(verbose_name="Роль", default=USER, choices=ROLE_TYPES)
    date_joined = models.DateTimeField(
        "Дата присоединения", blank=True, null=True, default=timezone.now
    )
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(
        default=True,
        verbose_name="Статус доступа",
    )

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []

    def save(self, *args, **kwargs):
        # Если пароль не хэширован, то хэшируем его перед сохранением
        if not self.password.startswith("pbkdf2_sha256"):
            self.password = make_password(self.password)
        super().save(*args, **kwargs)


class Card(models.Model):
    title = models.CharField(max_length=250, verbose_name="Название")
    text = models.TextField(verbose_name="Текст")
    image = models.ImageField(upload_to="images/%Y/%m/%d/")
    publish = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ["-publish"]
        indexes = [
            models.Index(fields=["-publish"]),
        ]

    def __str__(self) -> str:
        return self.title

    # def get_absolute_url(self):
    #     return reverse("blog:")


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to="users/%Y/%m/%d/", blank=True)

    def __str__(self) -> str:
        return f"Profile of {self.user.username}"


# user_model = get_user_model()
# user_model.set_password()
