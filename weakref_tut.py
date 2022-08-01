"""base idea of weak reference"""
import sys
import weakref

from utils import C

c = C()  # ref-counter increments to 1
d = weakref.ref(c)  # ref-counter increments to 2
sys.getrefcount(d)  # ref-counter remains at 2

v = c

assert d() is c  # these are the same object, d is a weak-ref

d()  # will not increase ref-count and will return none if garbage collected
