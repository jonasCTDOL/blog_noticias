#!/usr/bin/env python
import os, sys

# --- Start Debugging ---
# Create a debug file
debug_file_path = os.path.join(os.path.dirname(__file__), 'fcgi_debug.txt')
with open(debug_file_path, 'w') as f:
    f.write(f"Script started.\n")
    f.write(f"Python version: {sys.version}\n")
    f.write(f"Python path: {sys.path}\n")
# --- End Debugging ---

try:
    # Add the app's directory to the Python path
    sys.path.insert(0, os.path.dirname(__file__))
    
    with open(debug_file_path, 'a') as f:
        f.write("Attempting to import app...\n")

    from app import app

    with open(debug_file_path, 'a') as f:
        f.write("App imported successfully.\n")
        f.write("Attempting to import flup6...\n")

    from flup6.server.fcgi import WSGIServer

    with open(debug_file_path, 'a') as f:
        f.write("flup6 imported successfully.\n")
        f.write("Starting WSGIServer...\n")

    WSGIServer(app).run()

except Exception as e:
    with open(debug_file_path, 'a') as f:
        import traceback
        f.write("\n--- SCRIPT CRASHED ---\n")
        f.write(traceback.format_exc())
