"""base idea of weak reference dict"""
import weakref

from utils import C

dct = weakref.WeakKeyDictionary()

c = C()

dct[c] = 2

c = None  # object c is getting garbage collected
