from django.db import models
from django.contrib.auth.models import User
from PIL import Image
import os


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    image = models.ImageField(default='default.jpg', upload_to='profile_pics', verbose_name='Фотография')

    def __str__(self):  # Fixed method name
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):  # Added *args and **kwargs
        super().save(*args, **kwargs)  # Properly call the parent save method

        # Open the image file
        try:
            img = Image.open(self.image.path)

            # Resize the image if it exceeds the given size
            if img.height > 300 or img.width > 300:
                output_size = (300, 300)
                img.thumbnail(output_size)
                img.save(self.image.path)
        except Exception as e:
            print(f"Error resizing image: {e}")  # Error handling

    class Meta:
        verbose_name = "Профиль"
        verbose_name_plural = "Профили"
