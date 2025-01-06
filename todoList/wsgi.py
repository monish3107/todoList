import os
from django.core.wsgi import get_wsgi_application

# Set the default settings module for the 'django' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'todoList.settings')

# Ensure the app uses the correct port when running on Render.
port = os.getenv("PORT", "8000")
os.environ["PORT"] = port

# Get the WSGI application for Django.
application = get_wsgi_application()

# Alias it to 'app' for Render to recognize it.
app = application
