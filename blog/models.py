from django.db import models
from blog import utils, choices


class Region(utils.BaseModel):
    title = models.CharField(max_length=128)

    def __str__(self):
        return self.title


class District(utils.BaseModel):
    title = models.CharField(max_length=128)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Category(utils.BaseModel):
    title = models.CharField(max_length=256)
    slug = models.SlugField(unique=True, null=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title


class TypeCars(utils.BaseModel):
    title = models.CharField(max_length=128)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class CarModel(utils.BaseModel):
    title = models.CharField(max_length=128)
    year = models.DateField(help_text="Masalan, 1998 yoki 2007")
    price = models.IntegerField()
    is_less = models.CharField(max_length=32, choices=choices.IsLess, default=choices.IsLess.NO)
    fuel_type = models.CharField(max_length=64, choices=choices.FuelType, default=choices.FuelType.PETROL)
    transmission = models.CharField(max_length=128, choices=choices.Transmission)
    phone = models.CharField(max_length=32, unique=True)
    information = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='cars/', blank=True, null=True, help_text="Copy the file here.")

    volume = models.FloatField(blank=True, null=True, help_text="Masalan, 2.8 yoki 3")
    walking = models.FloatField(blank=True, null=True)
    color_status = models.CharField(max_length=128, choices=choices.ColorStatus, blank=True, null=True)
    extension = models.CharField(max_length=64, choices=choices.Extension, blank=True, null=True)

    outside = models.ManyToManyField(utils.Outside, blank=True, null=True)
    optical = models.ManyToManyField(utils.Optical, blank=True, null=True)
    salon = models.ManyToManyField(utils.Salon, blank=True, null=True)
    media = models.ManyToManyField(utils.Media, blank=True, null=True)
    vehicle_option = models.ManyToManyField(utils.VehicleOption, blank=True, null=True)
    additional = models.CharField(max_length=256, choices=choices.Additional, blank=True, null=True)



    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    car_type = models.ForeignKey(TypeCars, on_delete=models.CASCADE)
    color = models.ForeignKey(utils.Color, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.title


class Spare(utils.BaseModel):
    title = models.CharField(max_length=256)
    phone = models.CharField(max_length=32, unique=True)
    image = models.ImageField(upload_to='spare/', blank=True, null=True, help_text="Copy the file here.")
    information = models.TextField(blank=True, null=True)

    condition_spare = models.CharField(max_length=128, choices=choices.ConditionSpare)
    is_less = models.CharField(max_length=64, choices=choices.IsLess, default=choices.IsLess.NO)
    delivery = models.CharField(max_length=128, choices=choices.IsLess)

    car_type = models.ForeignKey(TypeCars, on_delete=models.CASCADE)
    car_year = models.ForeignKey(utils.SpareCarYear, on_delete=models.CASCADE, blank=True, null=True)
    car_model = models.ForeignKey(CarModel, on_delete=models.CASCADE)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    district = models.ForeignKey(District, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
