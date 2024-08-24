"""
WSGI config for politica project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os
import sys

# Ruta al directorio del proyecto Django
path = '/home/yoyo2024/politica'
if path not in sys.path:
    sys.path.append(path)

# Configuración del entorno de Django
os.environ['DJANGO_SETTINGS_MODULE'] = 'politica.settings'

# Activar el entorno virtual
activate_this = '/home/yoyo2024/.virtualenvs/mientorno/bin/activate_this.py'
exec(open(activate_this).read(), dict(__file__=activate_this))

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
