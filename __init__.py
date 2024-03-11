# This file is used to help expose what functions, classes, etc are available

# This python script will run EVERY TIME the module is imported and can contain
# any code you desire

# Here we're very simply making it easier for other scripts to access the
# to other scripts when the module is imported.
# process_files function. Note: other scripts and functions are still
# accessible
from .prepostfix import process_inputfile
