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
    kwargs = {'path': path,
              'template': 'dashboard/layout.html',
              'endpoint': '.dashboard'}

    return baip_munger_ui.staging_index.render_autoindex(**kwargs)


@baip_munger_ui.app.route('/munger/upload')
@baip_munger_ui.app.route('/munger/upload/<path:path>')
def upload(path='.'):
    """Munger upload.

    """
    kwargs = {'path': path,
              'template': 'dashboard/upload.html',
              'endpoint': '.upload'}

    return baip_munger_ui.staging_index.render_autoindex(**kwargs)


@baip_munger_ui.app.route('/munger/munge')
@baip_munger_ui.app.route('/munger/munge/<path:path>')
def munge(path='.'):
    """Munger munge.

    """
    kwargs = {'path': path,
              'template': 'dashboard/munge.html',
              'endpoint': '.munge'}

    return baip_munger_ui.staging_index.render_autoindex(**kwargs)


@baip_munger_ui.app.route('/munger/upload_file', methods=['GET', 'POST'])
def upload_file():
    if flask.request.method == 'POST':
        file_storage = flask.request.files['file']
        source_file = None

        if file_storage:
            source_file = file_storage.filename
            log_msg = 'File "%s" ' % source_file
            log.info('%s has been selected for upload' % log_msg)

            extensions = baip_munger_ui.app.config['ALLOWED_EXTENSIONS']
            if allowed_file(source_file, extensions):
                filename = werkzeug.secure_filename(source_file)
                target = os.path.join(baip_munger_ui.app.config['UPLOAD_DIR'],
                                      filename)
                file_storage.save(target)
                log.info('%s uploaded to "%s"' % (log_msg, target))

    return flask.redirect(flask.url_for('upload'))
