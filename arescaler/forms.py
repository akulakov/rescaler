from django import forms as f
from arescaler.models import *


class RescaleForm(f.Form):
    def __init__(self, *args, **kwargs):
        super(RescaleForm, self).__init__(*args, **kwargs)
        c = Item.objects.all()
        c = [(0, "---")] + [(c.pk, c.name) for c in c]

        self.fields["item1"].choices = c
        self.fields["item2"].choices = c

    item1 = f.ChoiceField(choices=())
    item2 = f.ChoiceField(choices=())
