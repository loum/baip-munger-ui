"""BAIP Munger UI views abstraction.
"""
import flask
import werkzeug
import os

import baip_munger_ui
from baip_munger_ui.utils import allowed_file
from logga.log import log


@baip_munger_ui.app.route('/munger/health')
def health():
    """Quick health check response

    """
    return flask.render_template('health.html')


@baip_munger_ui.app.route('/munger/dashboard')
@baip_munger_ui.app.route('/munger/dashboard/<path:path>')
def dashboard(path='.'):
    """Munger dashboard.

    """
    return baip_munger_ui.staging_index.render_autoindex(path=path,
                                                         template='dashboard/layout.html',
                                                         endpoint='.dashboard')


@baip_munger_ui.app.route('/munger/upload')
@baip_munger_ui.app.route('/autoindex/<path:path>')
def upload(path='.'):
    """Munger upload.

    """
    return baip_munger_ui.staging_index.render_autoindex(path=path,
                                                         template='dashboard/upload.html',
                                                         endpoint='.upload')


@baip_munger_ui.app.route('/munger/upload_file', methods=['GET', 'POST'])
def upload_file():
    if flask.request.method == 'POST':
        file = flask.request.files['file']
        extensions = baip_munger_ui.app.config['ALLOWED_EXTENSIONS']
        if file and allowed_file(file.filename, extensions):
            filename = werkzeug.secure_filename(file.filename)
            file.save(os.path.join(baip_munger_ui.app.config['UPLOAD_DIR'],
                                   filename))

        return flask.redirect(flask.url_for('upload'))
