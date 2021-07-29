from django.contrib import admin

# Register your models here.
from .models import Register_data, Uni_data
admin.site.register(Uni_data)
admin.site.register(Register_data)