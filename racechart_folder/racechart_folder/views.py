from django.shortcuts import render
from django.core.paginator import Paginator

from .models import Decade, Fad

def decade_list(request):
    decades = Decade.objects.all()
    return render(request, 'decade_list.html', {'decades': decades})

def fad_list(request):
    # fads = Fad.objects.all()
    paginator = Paginator(Fad.objects.all(), 2) # Show 2 contacts per page
    page = request.GET.get('page')
    fads = paginator.get_page(page)
    return render(request, 'fad_list.html', {'fads': fads})

def decade_detail(request, pk):
    decade = Decade.objects.get(id=pk)
    return render(request, 'decade_detail.html', {'decade': decade})

def fad_detail(request, pk):
    fad = Fad.objects.get(id=pk)
    return render(request, 'fad_detail.html', {'fad': fad})
