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
    conf_file = app.config['MUNGER_CONF_FILE']
    conf = baip_munger.XpathGen(conf_file=conf_file)
    app.config['MUNGER_ACTIONS'] = conf.parse_configuration()
except baip_munger.exception.MungerConfigError as e:
    log.error(str(e))

staging_index = AutoIndex(app,
                          browse_root=app.config['STAGING_DIR'],
                          add_url_rules=False)

ready_index = AutoIndex(app,
                        browse_root=app.config['READY_DIR'],
                        add_url_rules=False)

from baip_munger_ui import views
