from uuid import uuid4

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils.translation import gettext as _

from .managers import CustomUserManager


class User(AbstractBaseUser, PermissionsMixin):
    """Model definition for User."""

    id = models.UUIDField(
        _("id"),
        primary_key=True,
        default=uuid4,
        editable=False,
        db_index=True,
        unique=True,
    )
    email = models.EmailField(
        _("email address"),
        blank=True,
        db_index=True,
        unique=True,
    )
    first_name = models.CharField(
        _("first name"),
        max_length=150,
        blank=True,
    )
    last_name = models.CharField(_("last name"), max_length=150, blank=True)
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
    )
    bio = models.TextField(_("bio"), null=True, blank=True)
    avatar = models.ImageField(
        _("profile picture"),
        upload_to="images",
        null=True,
        blank=True,
    )
    created_at = models.DateTimeField(_("created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("updated at"), auto_now=True)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    class Meta:
        """Meta definition for User."""

        verbose_name = "User"
        verbose_name_plural = "Users"
