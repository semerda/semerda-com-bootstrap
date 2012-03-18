"""This is a skeleton settings_local.py file.  Copy it to settings_local.py and fill in the necessary information."""
from platform       import node
from os.path 		import join, dirname, normpath

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'enter_your_secret_key_here'

# Used to provide absolute paths.  Normally the default is fine.
LOCAL_PATH = normpath(join(dirname(__file__), '..'))

# These are the hostnames as returned by platform.node().
# If you aren't sure what to put, leave them blank and the error message should tell you which hostname Python sees.
DEVELOPMENT_HOST = 'ubuntu'     # local dev
PRODUCTION_HOST = 'semerda.com' # Production

# Used in template to determine which server is being hit
SERVER_NODE = node()