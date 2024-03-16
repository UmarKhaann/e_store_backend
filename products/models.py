from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    # image = models.FilePathField(path="/img")
    published_date = models.DateTimeField(auto_now_add=True)
    user_id = models.IntegerField()
    isRequest = models.fields.BooleanField(default=False)

    def __str__(self):
        return self.title