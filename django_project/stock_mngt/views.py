from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import *
from .forms import *

import csv


def home(request):
    title = "Hello everyone..."
    context = {
        "title": title
    }
    return render(request, "home.html", context)

@login_required
def list_items(request):
    title = "Items List"
    queryset = Stock.objects.all()
    form = StockSearchForm(request.POST or None)
    context = {
        "title": title,
        "queryset": queryset,
        "form": form
    }

    if request.method == "POST":
        queryset = Stock.objects.filter(  # category__icontains=form['category'].value(),
            item_name__icontains=form['item_name'].value())

        if form['export_to_csv'].value():
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="List of stocks.csv"'
            writer = csv.writer(response)
            writer.writerow(['CATEGORY', 'ITEM NAME', 'QUANTITY'])
            instance = queryset
            for stock in instance:
                writer.writerow([stock.category, stock.item_name, stock.quantity])

            return response

        context = {
            "title": title,
            "queryset": queryset,
            "form": form
        }

    return render(request, "list_items.html", context)

@login_required
def add_items(request):
    title = "Add Items"
    form = StockCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.info(request, "Saved successfully")
        return redirect('/list_items')
    context = {
        "title": title,
        "form": form
    }
    return render(request, "add_items.html", context)


def update_items(request, pk):
    queryset = Stock.objects.get(id=pk)
    form = StockUpdateForm(instance=queryset)
    if request.method == "POST":
        form = StockUpdateForm(request.POST, instance=queryset)

        if form.is_valid():
            form.save()
            messages.info(request, "Updated successfully")
            return redirect('/list_items')

    context = {
        "form": form
    }
    return render(request, 'add_items.html', context)


# delete items
def delete_items(request, pk):
    queryset = Stock.objects.get(id=pk)
    if request.method == "POST":
        queryset.delete()
        messages.info(request, "Deleted successfully")
        return redirect('/list_items')
    return render(request, 'delete_items.html')


# stock details
def stock_details(request, pk):
    queryset = Stock.objects.get(id=pk)
    context = {
        "queryset": queryset
    }
    return render(request, 'stock_details.html', context)


def issue_items(request, pk):
    queryset = Stock.objects.get(id=pk)
    form = IssueForm(request.POST or None, instance=queryset)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.quantity -= instance.issued_quantity
        instance.issued_by = str(request.user)

        if instance.quantity >= 0:
            instance.save()
            messages.info(request, f"Issued successfully. {instance.quantity} "
                                      f"{instance.item_name}s now left in store.")
        else:
            messages.info(request, "Insufficient stock avilable.")
        return redirect('/stock_details/' + str(instance.id))

    context = {
        "title": "Issue " + str(queryset.item_name),
        "queryset": queryset,
        "form": form,
        "username": "Issued by " + str(request.user)
    }
    return render(request, 'add_items.html', context)


def receive_items(request, pk):
    queryset = Stock.objects.get(id=pk)
    form = ReceiveForm(request.POST or None, instance=queryset)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.quantity += instance.received_quantity
        instance.save()
        messages.info(request, f"Received successfully. {instance.quantity} {instance.item_name}s now left in store.")

        return redirect('/stock_details/' + str(instance.id))

    context = {
        "title": "Receive " + str(queryset.item_name),
        "instance": queryset,
        "form": form,
        "username": "Received by " + str(request.user)
    }
    return render(request, 'add_items.html', context)

def stock_level(request, pk):
    queryset = Stock.objects.get(id=pk)
    form = StockLevelForm(request.POST or None, instance=queryset)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.info(request, f"Reorder level for  {instance.item_name} "
                                  f"{instance.stock_level} updated.")

        return redirect('/list_items')

    context = {
        "instance": queryset,
        "form": form
    }
    return render(request, 'add_items.html', context)