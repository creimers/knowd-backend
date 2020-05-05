from django.db import models
from django.contrib.auth import get_user_model

from taggit.managers import TaggableManager

UserModel = get_user_model()


class Note(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name="notes")
    content = models.TextField(blank=True, null=True)
    pinned = models.BooleanField(blank=True, default=False)
    favorite = models.BooleanField(blank=True, default=False)
    click_count = models.IntegerField(default=0)

    tags = TaggableManager()

    def __str__(self):
        return self.owner.email
