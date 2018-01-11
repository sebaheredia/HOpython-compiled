# -*- coding: utf-8 -*-
import ctypes as C
math = C.CDLL('./mymathlib.so')
math.add_int(1,2)
