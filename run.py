#!/usr/bin/python

# Get the 2.6 compatible verion of Jinja2
import sys
sys.path.insert(1, '/usr/lib/python2.6/site-packages/Jinja2-2.6-py2.6.egg')

sys.path.insert(1, '../baip-munger')

import baip_munger_ui


baip_munger_ui.app.run(host='0.0.0.0', debug=True)
