from django.db import models
from django.contrib import admin


class Email(models.Model):
    email = models.EmailField(max_length=254, unique=True)

    def __str__(self):
        return self.email


class ProductAdmin(admin.ModelAdmin):
    list_display = ['email']
    actions = ['Some future action (considered doing emails here)', ]

    def set_quantity_zero(self, request, queryset):
        print(list(queryset))
        for i in queryset:
            print(i)
        # SendEmail(queryset)

    set_quantity_zero.short_description = 'Set Quantity to Zero'
