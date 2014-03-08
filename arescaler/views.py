import json
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic.base import View
from django.views.generic.edit import FormView

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

    def Xget(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)

def do_rescale(request):
    items = Item.objects.all()
    post  = request.POST
    pk1   = int(post.get("item1"))
    pk2   = int(post.get("item2"))

    if pk1 and pk2:
        i1, i2 = Item.objects.get(pk=pk1), Item.objects.get(pk=pk2)
        items = Rescaler()._rescale(i1, i2, items)
        return json.dumps(dict(items=items))
    return json.dumps(None)
