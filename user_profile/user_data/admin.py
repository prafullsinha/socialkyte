from django.contrib import admin
from .models import ExcelModel, UserModel

# Register your models here.
admin.site.register(ExcelModel)
admin.site.register(UserModel)