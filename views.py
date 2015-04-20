from django.shortcuts import render_to_response
from django.template import RequestContext
import time
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render_to_response
from calendario.apps.cal.models import calendario

def index_view(request):
	return render_to_response('home/index.html',context_instance=RequestContext(request))

def about_view(request):
	mensaje = 'Esto es un mensaje desde mi vista'
	ctx = {'msg':mensaje} #msg es el nombre que ponemos en la plantilla '{{ msg }}' = mensaje
	return render_to_response('home/about.html',context_instance)RequestContext(request))


mnames = "Enero Febrero Marzo Abril Mayo Junio Julio Agosto Septiembre Octubre Noviembre Diciembre"
mnames = mnames.split()


@login_required
def principal(request, year=None):
    """Lista principal, anios y meses; 3 anios por pagina."""
    # anterior / siguiente anio
    if year: year = int(year)
    else:    year = time.localtime()[0]

    nowy, nowm = time.localtime()[:2]
    lst = []

    # crea una lista de meses de los anios,  indicando el contenido de las entradas
    for y in [year, year+1, year+2]:
        mlst = []
        for n, month in enumerate(mnames):
            entry = current = False   # es la entrada(s) durante el mes;
            entries = Entry.objects.filter(date__year=y, date__month=n+1)

            if entries:
                entry = True
            if y == nowy and n+1 == nowm:
                current = True
            mlst.append(dict(n=n+1, name=month, entry=entry, current=current))
        lst.append((y, mlst))

    return render_to_response("templates/principal.html", dict(years=lst, user=request.user, year=year,
                                                   reminders=reminders(request)))
