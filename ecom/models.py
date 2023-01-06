from django.db import models


# Create your models here.


class Media(models.Model):
    file = models.FileField(upload_to="media/%y/%m")
    name = models.CharField(max_length=50)

    def __str__(self):
        return "%s. %s" % (int(self.id), self.name)


class Category(models.Model):
    name = models.CharField(max_length=50)
    image = models.ForeignKey(Media, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s. %s" % (int(self.id), self.name)


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    discount_price = models.IntegerField()
    images = models.ManyToManyField(Media)
    quantity = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    desc = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s. %s" % (int(self.id), self.name)
