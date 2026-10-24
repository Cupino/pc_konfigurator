from django.db import models

class CPU(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    socket = models.CharField(max_length=50)
    ram_type = models.CharField(max_length=20)
    tdp = models.IntegerField()
    has_integrated_gpu = models.BooleanField(default=False)
    gaming_score = models.IntegerField(default=50)
    productivity_score = models.IntegerField(default=50)
    image_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name


class Motherboard(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    socket = models.CharField(max_length=50)
    ram_type = models.CharField(max_length=20)
    ram_slots = models.IntegerField(default=4)
    form_factor = models.CharField(max_length=20)
    image_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name


class RAM(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    ram_type = models.CharField(max_length=20)
    capacity_gb = models.IntegerField()
    module_count = models.IntegerField(default=2)
    speed_mhz = models.IntegerField()
    image_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name


class GPU(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    recommended_psu_wattage = models.IntegerField()
    tdp = models.IntegerField()
    length_mm = models.IntegerField()
    vram_gb = models.IntegerField()
    gaming_score = models.IntegerField(default=50)
    productivity_score = models.IntegerField(default=50)
    image_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name


class CPUCooler(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    supported_sockets = models.CharField(max_length=200)
    max_tdp = models.IntegerField()
    height_mm = models.IntegerField()
    cooler_type = models.CharField(max_length=20)
    radiator_size_mm = models.IntegerField(default=0, blank=True, null=True)
    image_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name


class Case(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    supported_form_factors = models.CharField(max_length=100)
    max_gpu_length_mm = models.IntegerField()
    max_cpu_cooler_height_mm = models.IntegerField()
    max_radiator_size_mm = models.IntegerField(default=0)
    image_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name


class Storage(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    drive_type = models.CharField(max_length=20)
    capacity_gb = models.IntegerField()
    image_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name


class PSU(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    wattage = models.IntegerField()
    efficiency_rating = models.CharField(max_length=50)
    form_factor = models.CharField(max_length=20, default="ATX")
    image_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name