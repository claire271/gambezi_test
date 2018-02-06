# The gambezi_python dir is expected to be a sibling directory of gambezi_test
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

# Open test, no reconnect ability
gambezi = Gambezi("localhost:5809", False)
test(gambezi.get_ready(), False, "Init start 1")
def on_ready(ws):
    print("on_ready:", ws)
    test(gambezi.get_ready(), True, "Init end 1")
gambezi.on_ready = on_ready

def on_error(obj):
    print("on_error:", obj)
gambezi.on_error = on_error

time.sleep(4)

# Close test, no reconnect ability
gambezi.close_connection()
test(gambezi.get_ready(), True, "Closed start 1")
def on_close(ws):
    print("on_close:", ws)
    test(gambezi.get_ready(), False, "Closed end 1")
gambezi.on_close = on_close

time.sleep(4)

# Open test, reconnect enabled
gambezi = Gambezi("localhost:5809", True, 2)
test(gambezi.get_ready(), False, "Init start 2")
def on_ready(ws):
    test(gambezi.get_ready(), True, "Init end 2")
gambezi.on_ready = on_ready

def on_error(obj):
    print("on_error:", obj)
gambezi.on_error = on_error

# Wait for disconnect to be certian
time.sleep(8)
test(gambezi.get_ready(), False, "Disconnect 1")
# Wait for restart of server
time.sleep(8)
test(gambezi.get_ready(), True, "Reconnect 1")

# Exit
sys.exit(0)
