from django.db import models
from django.utils import timezone
import re


# Create your models here.
class Entry(models.Model):
    title = models.CharField(max_length=40)
    content = models.TextField()
    slug = models.SlugField(db_index=True, unique=True, null=True, blank=True)
    pub_time = models.DateTimeField(default=timezone.now)

    def gen_slug(self):
        self.slug = re.sub('[^\w]+', '-', self.title.lower())
        self.save()

    def __str__(self):
        return self.title
