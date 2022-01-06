from django.db import models
from django.utils import timezone
from PIL import Image


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    has_images = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date_posted']


class PostImage(models.Model):
    post = models.ForeignKey(Post, default=None, on_delete=models.CASCADE)
    images = models.ImageField(upload_to="pictures")

    def save(self):  # already exists in models.Model but overwriting it
        super().save()  # run the parents class save

        file, ending = self.images.path.split(".")
        filename = file + ".jpeg"
        basewidth = 400
        img = Image.open(self.images.path)

        if ending in ["PNG", "png"]:
            img = img.convert('RGB')  # Convert to rgb
            img.save(file + ".jpeg")

        if img.height > 400 or img.width > 500:  # resize if necassary
            width = (basewidth / float(img.size[0]))
            height = int((float(img.size[1]) * float(width)))
            img = img.resize((basewidth, height), Image.ANTIALIAS)
            img.save(file + ".jpeg")

    def __str__(self):
        return str(self.post.pk)


class Video(models.Model):
    video_link = models.CharField(max_length=20)

    def __str__(self):
        return (self.video_link)
