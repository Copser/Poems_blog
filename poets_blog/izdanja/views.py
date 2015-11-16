from django.shortcuts import render_to_response
from django.template import RequestContext


# Create your views here.
def izdanja(request):
    """TODO: Docstring for izdanja.
    :returns: I'm just reterning a template
    to aplly bootstrap on it.
    This tamplete will display information
    about are profesor Pero Skoro.
    Sa oviom zelim da jednostavno prikazem
    stranicu koju cu da uredim sa Boostrap-om,
    na ovoj stranici je biti prikazani informacije
    o profesoru, njegovom ziotu i slicno.

    """
    return render_to_response('blog/izdanja.html',
                              context_instance=RequestContext(request))
