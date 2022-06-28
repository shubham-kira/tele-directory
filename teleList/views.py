from django.shortcuts import render
from .models import TeleItem


def master_list(request):
    master_list_items = TeleItem.objects.all()
    return render(request, 'teleList/master_list.html', {'master_list_items': master_list_items})
