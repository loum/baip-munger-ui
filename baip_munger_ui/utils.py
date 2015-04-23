import os

from logga.log import log

__all__ = ['allowed_file']


def allowed_file(filename, extensions):
    """Check if *filename* has an extension that is acceptable for upload.

    **Args:**
        *filename*: the textual representation of the file to upload

        *extensions*: list of accepted filename extension.  For example::

            ['html', 'htm', ...]

    **Returns:**
        Boolean ``True`` if extension is allowed.  ``False`` otherwise.

    """
    is_file_allowed = False

    extension = os.path.splitext(filename)[1].strip('.')

    log.debug('File name|valid extensions: "%s"|%s' %
              (filename, extensions))
    if extension in extensions:
        is_file_allowed = True

    log.info('File "%s" has accepted extension?: %s' %
             (filename, is_file_allowed))

    return is_file_allowed
