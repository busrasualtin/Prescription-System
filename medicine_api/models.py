from django.db import models

# Create your models here.
# medicine_api/models.py


import random

class New_Medicine(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def save(self, *args, **kwargs):
        # Eğer price alanı boşsa ve random bir değer atanmak isteniyorsa
        if self.price is None:
            # Belirlediğiniz bir fiyat aralığı içinde rastgele bir değer ata
            self.price = round(random.uniform(1, 300), 2)

        super(New_Medicine, self).save(*args, **kwargs)

