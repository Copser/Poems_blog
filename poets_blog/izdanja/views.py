from django.shortcuts import render_to_response
from django.template import RequestContext


# Create your views here.
def izdanja(request):
    """TODO: Docstring for izdanja.
    :returns: I'm just reterning a template
    to aplly bootstrap on it.
    This tamplete will dispaly Electrinc book
    and all future published book of the
    profesor.
    Sa oviom zelim da jednostavno prikazem
    stranicu koju cu da uredim sa Boostrap-om,
    na ovoj stranici je biti prikazani sva
    profesorova izdanja, kao i elektronska
    knjiga koju je napisao.

    """
    return render_to_response('blog/flipbook/izdanja.html',
                              context_instance=RequestContext(request))
