"""base idea of weak reference used for circular ref and proxy weak ref"""
import weakref

from utils import C

c = C()
c.x = 1
c.c = weakref.proxy(c)  # gets instance (no need to be called to get an object)

c.c.c.c.c.c.c.c.x  # circular ref at it's fines

c = None  # gc immediately since weak-ref does not increase ref-count
