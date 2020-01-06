# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)

import uos, machine
#uos.dupterm(None, 1) # disable REPL on UART(0)

from lib.decouple import config
if config('WEBREPL_PASSWORD', False):
    import webrepl
    webrepl.start()

import gc
gc.collect()
