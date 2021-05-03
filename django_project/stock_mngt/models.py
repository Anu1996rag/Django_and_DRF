from django.db import models

category_choice = (
    ('Computer Peripherals', 'Computer Peripherals'),
    ('Stationery', 'Stationery'),
)


# creating category table
class Category(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name


# creating table Stock
class Stock(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True)
    item_name = models.CharField(max_length=50, blank=True, null=True)
    quantity = models.IntegerField(default='0', blank=True, null=True)
    received_quantity = models.IntegerField(default='0', blank=True, null=True)
    received_by = models.CharField(max_length=50, blank=True, null=True)
    issued_quantity = models.IntegerField(default='0', blank=True, null=True)
    issued_by = models.CharField(max_length=50, blank=True, null=True)
    issued_to = models.CharField(max_length=50, blank=True, null=True)
    contact_no = models.CharField(max_length=10, blank=True, null=True)
    stock_level = models.IntegerField(default='0', blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True, auto_now=False)
    last_updated = models.DateTimeField(auto_now_add=False,auto_now=True)

    def __str__(self):
        return self.item_name + " : " + str(self.quantity)

