from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    USER = "user"
    ADMIN = "admin"

    ROLES = [
        (USER, "Пользователь"),
        (ADMIN, "Администратор"),
    ]

    email = models.EmailField(
        max_length=254,
        unique=True,
        verbose_name="Адрес электронной почты",
    )
    role = models.CharField(
        max_length=16,
        choices=ROLES,
        default=USER,
        verbose_name="Роль пользователя",
    )

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    @property
    def is_admin(self):
        return self.role == User.ADMIN or self.is_superuser or self.is_staff

    def __str__(self):
        return self.username


class Follow(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Пользователь",
        related_name="follower",
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Автор",
        related_name="following",
    )

    class Meta:
        verbose_name = "Подписка"
        verbose_name_plural = "Подписки"
        constraints = [
            models.UniqueConstraint(
                fields=["user", "author"], name="unique_following"
            ),
        ]

    def __str__(self):
        return f"{self.user} follows {self.author}"
