#!/usr/bin/env python
import os, sys
from flup6.server.fcgi import WSGIServer
# Add the app's directory to the Python path
sys.path.insert(0, os.path.dirname(__file__))
# Import the Flask app instance
from app import app
# The WSGIServer needs a callable
WSGIServer(app).run()