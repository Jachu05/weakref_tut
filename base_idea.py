"""base idea of reference counting and simple garbage collection"""
import sys

from utils import C

a = C()  # ref-counter increments to 1
sys.getrefcount(a)  # ref-counter increments to 2

b = a  # ref-counter increments to 3
sys.getrefcount(a)  # ref-counter remains at 3
sys.getrefcount(a)  # ref-counter remains at 3
sys.getrefcount(a)  # ref-counter remains at 3

b = None
sys.getrefcount(a)  # ref-counter decreased to 2

a = None  # object is getting garbage collected
