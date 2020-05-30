from django.contrib import admin
from .models import Publication

admin.site.site_header = "Administración del kubOyect"
admin.site.register(Publication)