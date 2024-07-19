from django.db import models
from django.contrib.auth.models import User
from random import sample
import string


class Category(models.Model):
    name = models.CharField(max_length=255)
    generate_code = models.CharField(max_length=255, blank=True,unique=True)

    def __str__(self) -> str:
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.generate_code = "".join(sample(string.ascii_letters, 20))
        super(Category, self).save(*args, **kwargs)