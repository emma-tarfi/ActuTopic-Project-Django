from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.text import slugify

STATUS = (
    (0, "Brouillon"),
    (1, "Publier")
)


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(default='', max_length=500)
    author = models.ForeignKey(User, on_delete= models.CASCADE, related_name='blog_posts')
    image = models.ImageField(upload_to='images_posts/', blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        kwargs = {
            'pk': self.id,
            'slug': self.slug
        }
        return reverse('post_detail', kwargs=kwargs)

    def save(self, *args, **kwargs):
        value = self.title
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)
