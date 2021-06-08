from django.contrib.auth.models import User
from django.db import models
from django.template.defaultfilters import slugify as django_slugify
from django.urls import reverse
from django.utils import timezone

alphabet = {'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'yo', 'ж': 'zh', 'з': 'z', 'и': 'i',
            'й': 'j', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't',
            'у': 'u', 'ф': 'f', 'х': 'kh', 'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch', 'ы': 'i', 'э': 'e', 'ю': 'yu',
            'я': 'ya'}


def slugify(s):
    """
    Overriding django slugify that allows to use russian words as well.
    """
    return django_slugify(''.join(alphabet.get(w, w) for w in s.lower()))


# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=60, default='Default title')
    text = models.TextField(max_length=255, default='Default text')
    published = models.DateTimeField(default=timezone.now())
    slug = models.SlugField(default='', max_length=60, unique=True)

    class Meta:
        ordering = ['-published']

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title + str(self.author.id) + str(self.published.second) + str(self.published.minute))
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail_post', args=[str(self.slug)])


class Role(models.Model):
    name = models.CharField(max_length=60)
    users = models.ManyToManyField(User)

    def __str__(self):
        return self.name
