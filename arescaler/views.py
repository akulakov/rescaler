import json
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic.base import View
from django.views.generic.edit import FormView
from django.core.urlresolvers import reverse

from arescaler.forms import RescaleForm
from arescaler.models import Item
from rescaler import sizes, Rescaler

def main(request):
    n = 0
    for size in sizes.values():
        i, created = Item.objects.get_or_create(name=size.name, size=size.size)
        n += int(created)
    return HttpResponse("%s items added" % n)

class RescaleView(FormView):
    template_name = "rescale.html"
    form_class = RescaleForm


def do_rescale(request):
    items = Item.objects.all()
    post  = request.POST
    pk1   = int(post.get("item1"))
    pk2   = int(post.get("item2"))
    data  = None

    if pk1 and pk2:
        i1, i2 = Item.objects.get(pk=pk1), Item.objects.get(pk=pk2)
        items  = Rescaler()._rescale(i1, i2, items)
        table  = "<table cellpadding='5' cellspacing='4'>%s</table>"
        item   = "<tr><td>%s</td><td>%s</td></tr>"
        items  = [item % i for i in items if i[0]]
        items  = '\n'.join(items)
        items  = table % items
        data   = dict(items=items)

    return HttpResponse(json.dumps(data), content_type="application/json")
