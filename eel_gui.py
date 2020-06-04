from __future__ import print_function	# For Py2/3 compatibility
import eel
import recipes as rp

eel.init('web')                     # Give folder containing web files

@eel.expose                         # Expose this function to Javascript
def say_helo_py(x):
    print('Yo from %s' % x)

eel.say_hello_js('connected!')   # Call a Javascript function

eel.start('main.html', size=(500, 400))    # Start
