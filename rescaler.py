#!/usr/bin/env python
# -*- encoding: utf-8 -*-

""" Rescaler

by: andrei.avk@gmail.com
license: (see LICENSE file)
"""

from __future__ import print_function, unicode_literals, division
import os, sys
from copy import copy
from utils import Container, nl

sizes = [
         (1, "ant", 0.01),
         (2, "doorway", 1),
         (3, "baseball bat", 1),
         (5, "whale", 10),
         (6, "city block", 100),
         (7, "Eiffel tower", 300),
         (8, "English channel (narrowest)", 35000),
         (9, "AU (Earth to Sun)", 1.5e11),
         (10, "Light Year", 9.5e15),

         (11, "Earth", 1.2e7),
         (12, "Height of Everest", 8.8e3),
         (13, "Jupiter", 1.4e8),
         (14, "Distance to the Moon", 3.8e8),
         (15, "Sun", 1.4e9),
         (16, "Betelgeuse", 1.0e12),
         (17, "Distance from Sun to Pluto", 5.9e12),
         (18, "Nearest star to Earth (except for Sun)", 4.10e16),
         (19, "Crab nebula", 9.0e16),

         (21, "thickness of sunglasses", 0.001),
         (22, "Staphilococcus bacterium", 1e-6),
         (23, "Poliovirus", 3e-8),
         (24, "Hydrogen atom", 1e-10),
         (25, "Hydrogen nucleus", 2.4e-15),

         (26, "Typical globular cluster", 3.0e+18),
         (27, "Distance from Sun to Galactic center", 2.4e+20),
         (28, "Milky Way", 7.8e+20),
     ]

sizes = {s[0]: Container(name=s[1], size=s[2]) for s in sizes}

unit_table = {
              (None, 1e-9)       : "less than a nanometer",
              (1e-9, 1e-6)       : "%s nanometer%s",
              (1e-6, 1e-3)       : "%s micrometer%s",
              (1e-3, 1e-2)       : "%s millimeter%s",
              (1e-2, 1e+0)       : "%s centimeter%s",
              (1e+0, 1e+3)       : "%s meter%s",
              (1e+3, 1.5e+11)    : "%s kilometer%s",
              (1.5e+11, 9.5e+15) : "%s AU%s",
              (9.5e+15, None)    : "%s Light years%s",
              }


class Rescaler(object):
    tpl = "%-38s %s"
    msg = "If %s was the size of %s" + nl*2

    def rescale(self, i1, i2):
        """Wrapper method used from command line."""
        i1, i2 = sizes[i1], sizes[i2]
        print(self.msg % (i1.name, i2.name))
        for name, val in self._rescale(i1, i2, sizes.values()):
            if name:
                print(self.tpl % (name, val))

    def _rescale(self, i1, i2, items):
        """Return rescaled name/size pairs."""
        ratio = i1.size / i2.size

        for item in items:
            if item == i1: continue
            size = item.size / ratio
            val  = self.format(size)
            if val:
                yield item.name, val
            else:
                yield None, None

    def format(self, val):
        def fmt(val):
            plural = '' if val==1 else 's'
            val = ("%.2f" % val).rstrip('0').rstrip('.')
            return val, plural

        for (frm, to), unit in unit_table.items():
            if to and frm:
                if frm <= val < to:
                    return unit % fmt( val * (1/frm) )
            else:
                if to and val < to:
                    return None
                    # return unit
                if frm and val >= frm:
                    return unit % fmt( val * (1/frm) )


if __name__ == "__main__":
    arg = sys.argv[1:]
    try:
        Rescaler().rescale(int(arg[0]), int(arg[1]))
    except KeyboardInterrupt:
        pass
