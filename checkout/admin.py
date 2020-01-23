from django.contrib import admin
from .models import Order, OrderLineItem, Purchases


class OrderLineAdminInline(admin.TabularInline):
    model = OrderLineItem


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineAdminInline,)


admin.site.register(Order, OrderAdmin)
admin.site.register(Purchases)