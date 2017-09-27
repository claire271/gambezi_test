# The gambezi_python dir is expected to be a child directory of gambezi_test
import sys
import os
sys.path.insert(1, os.path.join(sys.path[0], '..'))

# Imports
from gambezi_python import Gambezi
import time

# Helpers
def test(given, expected, message):
    if given != expected:
        print("{0}: Expected {1} != {2}".format(message, expected, given))

# Open test
gambezi = Gambezi("localhost:7709", False)
test(False, gambezi.is_ready(), "Init start")
def on_ready(ws):
    print("READY")
    test(True, gambezi.is_ready(), "Init finished")
gambezi.on_ready = on_ready

# Queue test
a = gambezi.register_key(['a'])
#test([-1], a.get_key()
a.on_ready = lambda: print(a.get_key())
a.update_subscription(0x0001)


time.sleep(5)


# Close test
gambezi.close_connection()
test(True, gambezi.is_ready(), "Closed called")
def on_close(ws):
    print("CLOSED")
    test(False, gambezi.is_ready(), "Closed finished")
gambezi.on_close = on_close
