CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

UPLOAD_DIR = '/tmp/uploads'
ALLOWED_EXTENSIONS = set(['html', 'htm'])

# Munger staging directory on the server.
# STAGING_DIR = '/data/share/baip-munger/staging'
STAGING_DIR = '/var/tmp/uploads'

# Munger ready directory on the server.
READY_DIR = '/var/tmp/ready'

# Define the location of the Munger configuration file.
MUNGER_CONF_FILE = 'baip_munger_ui/tests/files/baip-munger.xml'

# Munger is ready for processing.
MUNGER_ACTIONS = None
