from django.contrib import admin

from .models import ShopItem


class ShopItemAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "category")
    list_filter = ("category",)
    search_fields = ("name",)

admin.site.register(ShopItem, ShopItemAdmin)