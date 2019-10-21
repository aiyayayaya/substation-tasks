from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Substation

def index(request):
    substation_name = Substation.objects.order_by('name')
    template = loader.get_template('showdata/index.html')
    substationId = request.POST.get('station', 'Lovelace Road')
    print(request)
    results = Substation.objects.filter(name=substationId)
    context = {
        'substation_name': substation_name,
        'results': results
    }
    return HttpResponse(template.render(context, request))
