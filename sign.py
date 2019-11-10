#! python

import sys
from alphasign import alphasign


sign = alphasign.Serial()

sign.connect()
sign.beep(1, 1, 1)