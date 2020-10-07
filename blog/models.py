from django.db import models
from django.utils import timezone
import re


# Create your models here.
class Entry(models.Model):
    title = models.CharField(max_length=40)
    entry_text = models.TextField()
    slug = models.CharField(unique=True, max_length=40, editable=False)
    pub_time = models.DateTimeField(default=timezone.now)

    def gen_slug(self):
        self.slug = re.sub('[^\w]+', '-', self.title.lower())
        self.save()
