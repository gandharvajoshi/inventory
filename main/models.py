from django.db import models
class Inventory(models.Model):
    name = models.CharField(max_length=100)
    quantity  = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Inventory Item"
