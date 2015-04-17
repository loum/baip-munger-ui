"""GeoLib web interface.

"""
import flask
from flask.ext.autoindex import AutoIndex


app = flask.Flask(__name__)
app.config.from_object('config')

staging_index = AutoIndex(app,
                          browse_root=app.config['STAGING_DIR'],
                          add_url_rules=False)

from baip_munger_ui import views
