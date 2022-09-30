from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from racks.models import django_rack

def index(request):
    items = django_rack.objects.all()
    return render(request, 'the_stores/index.html',{
        'items': items,
         })



def item_detail(request,id):
    try:
        item=django_rack.objects.get(id=id)
    except Item.DoesNotExit:
         raise Http404('This item does not exit')
    return render(request,'the_stores/item_detail.html',{
        'item':item,
 })

