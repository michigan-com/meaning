import sys
import os.path
activate_this = '/opt/.virtualenvs/meaning/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))
sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)))
from meaning import app as application
