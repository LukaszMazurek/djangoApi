from django.db import models



class Gallery(models.Model):
    gallery_name = models.CharField(max_length=128)

    def __str__(self):
        return self.gallery_name

class Image(models.Model):
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=128)
    date = models.DateField(auto_now_add=True)
    path = models.CharField(max_length=128)
    size = models.IntegerField
    gallery = models.ForeignKey(Gallery, default=1, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

