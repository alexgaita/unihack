from django.contrib import admin
from cantina.models import Person
# Register your models here.
class AuthorAdmin(admin.ModelAdmin):
    pass
admin.site.register(Person, AuthorAdmin)
