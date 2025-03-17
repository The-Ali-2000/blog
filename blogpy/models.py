from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from datetime import datetime


def validate_file_extension(value):
    import os
    from django.core.exceptions import ValidationError
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.jpg', '.png', '.jpeg', '.gif', '.svg', '.webp']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension.')


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.FileField(upload_to='files/avatars', null=True, blank=True, validators=[validate_file_extension])
    description = models.CharField(max_length=500, null=False, blank=False)


class Article(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False)
    cover = models.FileField(upload_to='files/files_covers', null=False, blank=False, validators=[validate_file_extension])
    content = RichTextField()
    created_at = models.DateTimeField(default=datetime.now)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    author = models.OneToOneField(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False)
    cover = models.FileField(upload_to='files/files_categories', null=False, blank=False, validators=[validate_file_extension])
    description = models.CharField(max_length=500, null=False, blank=False)

    def __str__(self):
        return self.title
  