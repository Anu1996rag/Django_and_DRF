from django import forms
from .models import Stock


class StockCreateForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['category', 'item_name', 'quantity']

    def clean_category(self):
        category = self.cleaned_data.get('category')
        if not category:  # if the category is empty
            raise forms.ValidationError("This field is required.")

        for instance in Stock.objects.all():
            if instance.category == instance:
                raise forms.ValidationError(category + "is already created.")
        return category

    def clean_item_name(self):
        item_name = self.cleaned_data.get('item_name')
        if not item_name:
            raise forms.ValidationError("This field is required.")

        return item_name


# to search in the list item table
class StockSearchForm(forms.ModelForm):
    export_to_csv = forms.BooleanField(required=False)
    class Meta:
        model = Stock
        fields = ['category', 'item_name']


# to update the list item table
class StockUpdateForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['category', 'item_name', 'quantity']

class IssueForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['issued_quantity', 'issued_to']

class ReceiveForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['received_quantity', 'received_by']

class StockLevelForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['stock_level']