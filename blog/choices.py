from django.db import models


class IsLess(models.TextChoices):
    YES = "Ha"
    NO = "Yo'q"


class FuelType(models.TextChoices):
    PETROL = "Benzin"
    GAZ_GASOLINE = "Gaz benzin"
    DIESEL = "Dizel"
    ELECTRIC = "Elektr"
    HYBRID = "Gibrid"
    GAS = "Gaz"


class Transmission(models.TextChoices):
    MECHANIC = 'Mexanika'
    AUTOMATIC = 'Avtomat'
    TIPTRONICS = 'Tiptronik'
    DIAMMER = 'Variator'
    ROBOT = 'Robot'


class ColorStatus(models.TextChoices):
    CLEAR = "Kraska toza"
    HAS = "Kraskasi bor"
    PYATNO = "Petno bor"
    FULL = "To'liq kraska"


class Extension(models.TextChoices):
    BEFORE = "Oldi"
    BACK = "Orqa"
    FULL = "To'liq"


class Additional(models.TextChoices):
    TESTED = "Texnik ko'rikdan o'tgan"
    SPEND_MONEY = "Pul sarflashning hojati yo'q"


class ConditionSpare(models.TextChoices):
    NEW = 'Yangi'
    USED = "Islatilgan"

