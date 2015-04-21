"""BAIP Munger web user interface.

"""
import flask
from flask.ext.autoindex import AutoIndex

from logga.log import log
import baip_munger
import baip_munger.exception


app = flask.Flask(__name__)
app.config.from_object('config')

# Load the Munger config.
try:
    conf = baip_munger.XpathGen()
    app.config['MUNGER_CONF'] = conf.parse_configuration()
except baip_munger.exception.MungerConfigError as e:
    log.error(str(e))

staging_index = AutoIndex(app,
                          browse_root=app.config['STAGING_DIR'],
                          add_url_rules=False)

from baip_munger_ui import views
