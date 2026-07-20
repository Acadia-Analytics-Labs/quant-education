"""Put the app/ directory on sys.path so tests can import the app modules."""
import pathlib
import sys

APP_DIR = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(APP_DIR))
