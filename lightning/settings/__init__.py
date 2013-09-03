import os.path
import os

settings_file = 'base_settings.py'

execfile(os.path.join(os.path.dirname(__file__), settings_file))
