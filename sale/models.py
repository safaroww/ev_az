from django.db import models

# Create your models here.


class City(models.Model):
    title = models.CharField(max_length=100)
   
    def __str__(self):
        return self.title 
class PropertyType(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title
class PurchaseType(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title
class Property(models.Model):
    title = models.CharField(max_length=100)
    price = models.IntegerField()
    info = models.TextField()
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True, blank=True)
    video_id = models.CharField(max_length=100, null=True, blank=True)
    kmetr = models.FloatField()
    type = models.ForeignKey(PropertyType, on_delete=models.SET_NULL, null=True, blank=True)
    purchase = models.ForeignKey(PurchaseType, on_delete=models.SET_NULL, null=True, blank=True)
    new = models.BooleanField()
    repaired = models.BooleanField()
    longitude = models.CharField(max_length=100, null=True, blank=True)
    lattitude = models.CharField(max_length=100, null=True, blank=True)
    updated = models.DateField(auto_now=True)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    def get_main_image(self):
        result = self.images.filter(main=True).first()
        if result:
            return result
        else:
            return self.images.first()
    
class PropertyFeature(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    
class PorpertyImage(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='property-image/')
    main = models.BooleanField(default=False)
    
    def save(self):
        if self.main:
            self.property.images.all().update(main=False)
        super().save()
        
    def delete(self):
        other = self.property.images.exclude(pk=self.pk).first()
        if other:
            other.main = True
            other.save()
        super().delete()