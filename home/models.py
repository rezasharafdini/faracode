from django.db import models
from django.utils.html import format_html


class Portfolio(models.Model):
    title = models.CharField(max_length=40)
    description = models.CharField(max_length=100)
    image = models.ImageField(upload_to='portfilio/images')
    is_publish = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}:{self.description[:30]}'

    def show_image(self):
        return format_html(f'<img src="{self.image.url}" width="50px" height="50px"')
    show_image.short_description = 'image'
