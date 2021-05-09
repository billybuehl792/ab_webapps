import os
import sys
import logging

activate_this = os.path.dirname(__file__) + '/venv/bin/activate_this.py'
with open(activate_this, 'r') as f:
    data = f.read()

exec(data, {'__file__': activate_this})

logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/ab_site/")

from ab_site import app as application
application.secret_key = 'busterTheRat2020'
