from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=128)
    model_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
