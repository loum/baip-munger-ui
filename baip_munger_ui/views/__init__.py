"""BAIP Munger UI views abstraction.
"""
import flask
import werkzeug
import os

import baip_munger_ui
import baip_munger
from baip_munger_ui.utils import allowed_file
from logga.log import log
from filer.files import get_directory_files_list


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
    extensions = baip_munger_ui.app.config['ALLOWED_EXTENSIONS']
    extensions_formatted = ', '.join(['*.%s' % ext for ext in extensions])
    accept_formatted = ','.join(['.%s' % ext for ext in extensions])
    kwargs = {
        'path': path,
        'template': 'dashboard/upload.html',
        'template_context': {
            'extensions': extensions_formatted,
            'accept': accept_formatted,
        },
        'endpoint': '.upload'
    }

    return baip_munger_ui.staging_index.render_autoindex(**kwargs)


@baip_munger_ui.app.route('/munger/munge')
@baip_munger_ui.app.route('/munger/munge/<path:path>')
def munge(path='.'):
    """Munger munge.

    """
    enabled = baip_munger_ui.app.config['MUNGER_ACTIONS'] is not None,
    kwargs = {
        'path': path,
        'template': 'dashboard/munge.html',
        'template_context': {
            'enabled': enabled,
        },
        'endpoint': '.munge',
    }

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


@baip_munger_ui.app.route('/munger/munge_files', methods=['POST'])
def munge_files():
    """Munge files.

    """
    in_dir = baip_munger_ui.app.config['STAGING_DIR']
    log.debug('Munging files: %s' % get_directory_files_list(in_dir))

    for html_file in get_directory_files_list(in_dir):
        target_file = os.path.join(baip_munger_ui.app.config['READY_DIR'],
                                   os.path.basename(html_file))

        munger = baip_munger.Munger()
        munger.munge(baip_munger_ui.app.config['MUNGER_ACTIONS'],
                     html_file,
                     target_file)

    return flask.redirect(flask.url_for('munge'))


@baip_munger_ui.app.route('/munger/download')
@baip_munger_ui.app.route('/munger/download/<path:path>')
def download(path='.'):
    """Munger download.

    """
    kwargs = {
        'path': path,
        'template': 'dashboard/download.html',
        'endpoint': '.download'
    }

    return baip_munger_ui.ready_index.render_autoindex(**kwargs)
