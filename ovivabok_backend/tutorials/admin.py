from django.contrib import admin
from .models import *

admin.site.site_header = "OvivaBok Administration"
admin.site.site_title = "OvivaBok Admin Portal"
admin.site.index_title = "Welcome to OvivaBok Admin"

admin.site.register(Course)
admin.site.register(Tutorial)

# Register your models here.
