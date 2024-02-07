from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    update_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class CarBody(BaseModel):
    title = models.CharField(max_length=128)

    def __str__(self):
        return self.title


class Position(BaseModel):
    title = models.CharField(max_length=128)

    def __str__(self):
        return self.title


class Color(BaseModel):
    title = models.CharField(max_length=128)

    def __str__(self):
        return self.title


class Outside(BaseModel):
    title = models.CharField(max_length=128)

    def __str__(self):
        return self.title


class Optical(BaseModel):
    title = models.CharField(max_length=128)

    def __str__(self):
        return self.title


class Salon(BaseModel):
    title = models.CharField(max_length=128)

    def __str__(self):
        return self.title


class Media(BaseModel):
    title = models.CharField(max_length=128)

    def __str__(self):
        return self.title


class VehicleOption(BaseModel):
    title = models.CharField(max_length=128)

    def __str__(self):
        return self.title


class SpareCarYear(BaseModel):
    title = models.CharField(max_length=256)

    def __str__(self):
        return self.title


class SpareType(BaseModel):
    title = models.CharField(max_length=256)

    def __str__(self):
        return self.title
