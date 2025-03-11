from django.db import models # type: ignore

# Create your models here.
class Item(models.Model):
    item_name = models.CharField(max_length = 100)
    item_desc = models.CharField(max_length = 100)
    price = models.IntegerField()
    item_image = models.URLField(default="https://e7.pngegg.com/pngimages/599/45/png-clipart-computer-icons-loading-chart-hand-circle.png")
    
