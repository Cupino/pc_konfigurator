from django.contrib import admin
from .models import CPU, Motherboard, RAM, GPU, CPUCooler, Case, Storage, PSU

admin.site.register(CPU)
admin.site.register(Motherboard)
admin.site.register(RAM)
admin.site.register(GPU)
admin.site.register(CPUCooler)
admin.site.register(Case)
admin.site.register(Storage)
admin.site.register(PSU)