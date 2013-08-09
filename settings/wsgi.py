import os
import sys


PROJECT_DIR = os.path.dirname(os.path.realpath(__file__))
sys.path.append(PROJECT_DIR)
_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(PROJECT_DIR,os.path.dirname(os.path.abspath(_dir))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings.settings")


from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
