#! /home/ssmiley/IdeaProjects/batcave/venv/bin/python

import logging
import sys
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, '/src')
sys.path.append('/venv/lib/python3.8/site-packages')
from zap import app as application
application.secret_key = 'nuts to you'