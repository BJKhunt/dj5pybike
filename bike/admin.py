from django.contrib import admin
from .models import Cate, Prod, Rev

# Register your models here.

admin.site.register(Prod)
admin.site.register(Cate)
admin.site.register(Rev)