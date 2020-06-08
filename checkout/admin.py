from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineAdminInline(admin.TabularInline):
    """
    Class to set up the layout of product information
    for each line in the admin panel
    """

    model = OrderLineItem


class OrderAdmin(admin.ModelAdmin):
    """Class to organise the lines of items within the admin panel"""


# Setting up access through django admin panel
admin.site.register(Order, OrderAdmin)
