from django.contrib import admin

# Register your models here.
from .models import Stock, Category
from .forms import StockCreateForm


class StockCreateAdmin(admin.ModelAdmin):
    list_display = ['category', 'item_name', 'quantity', 'stock_level', 'last_updated']
    form = StockCreateForm
    list_filter = ['category']
    search_fields = ['category', 'item_name']


admin.site.register(Stock, StockCreateAdmin)
admin.site.register(Category)