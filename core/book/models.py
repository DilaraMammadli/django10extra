from django.db import models



class Book(models.Model):

    name = models.CharField(max_length=300)
    description = models.TextField(blank=True, null=True)
    price=models.FloatField()
    discount_price=models.FloatField(blank=True, null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



    def __str__(self):
        return self.name