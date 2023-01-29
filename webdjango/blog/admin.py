from django.contrib import admin
from .models import comic
from .models import member
# Register your models here.

admin.site.register(comic)
admin.site.register(member)