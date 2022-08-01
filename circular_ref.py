"""base idea of weak reference used for circular ref"""
import gc

from utils import C

c = C()
c.c = c

c.c.c.c.c.c.c.c  # circular ref at it's fines

c = None  # will not be gc immediately

gc.collect()  # finds and gc circular ref
