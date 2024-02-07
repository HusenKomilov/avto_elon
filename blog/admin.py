from django.contrib import admin
from blog.models import Region, District, TypeCars, CarModel, Spare, Category
from blog.utils import CarBody, Position, Color, Outside, Optical, Salon, Media, VehicleOption

admin.site.register(
    [Region, District, TypeCars, CarModel, Spare, CarBody, Position, Color, Outside, Optical, Salon, Media,
     VehicleOption])


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'parent')
    prepopulated_fields = {'slug': ('title',)}
