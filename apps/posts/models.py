from enum import Enum
from uuid import uuid4

from django.db import models
from django.utils.translation import gettext as _

from apps.accounts.models import User


class Status(Enum):
    DRAFT = "draft"
    PUBLISHED = "published"
    ARCHIVED = "archived"

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]


class Post(models.Model):
    """Model definition for Post."""

    id = models.UUIDField(
        _("id"),
        default=uuid4,
        primary_key=True,
        editable=False,
        unique=True,
        db_index=True,
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(_("title"), max_length=255, db_index=True)
    content = models.TextField(_("content"))
    featured_image = models.ImageField(_("featured image"), upload_to="images")
    created_at = models.DateTimeField(_("created at"), auto_now=True)
    updated_at = models.DateTimeField(_("updated at"), auto_now_add=True)
    status = models.CharField(
        _("status"),
        max_length=11,
        choices=Status.choices(),
        default=Status.DRAFT,
    )
    likes = models.IntegerField(_("likes"))

    class Meta:
        """Meta definition for Post."""

        verbose_name = "Post"
        verbose_name_plural = "Posts"

    def __str__(self):
        """Unicode representation of Post."""
        return self.title
