from django.db import models

class Item(models.Model):
    name  = models.CharField(max_length=120)
    size  = models.FloatField()
    notes = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ("size",)
