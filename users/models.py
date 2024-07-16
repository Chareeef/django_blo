from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    """Profile model
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(
        default='profile_pics/default.jpg', upload_to='profile_pics')

    def save(self):
        """Override save method to resize large images
        """
        super().save()

        # Check the image's size
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            # Resize and save
            img.thumbnail((300, 300))
            img.save(self.image.path)

    def __repr__(self):
        """Profile's literal representation
        """
        return f"{self.user.username}'s Profile"