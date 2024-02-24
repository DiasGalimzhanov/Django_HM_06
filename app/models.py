from django.db import models

class Brand(models.Model):
    name = models.CharField(max_length = 255)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Автомобиль'
        verbose_name_plural = 'Автомобили'

class Models(models.Model):
    class Status(models.TextChoices):
        new = 'nw', 'Новая'
        not_new = 'nn', 'Б/У'

    model = models.CharField(max_length =255)
    volume = models.IntegerField()
    cover = models.ImageField(upload_to='covers/',default = 'covers/not.png')
    price = models.IntegerField()
    status = models.CharField(max_length=2, choices=Status.choices, default = Status.new)
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.brand} {self.model} {self.status} - {self.price}"
