import platform
import django
import sqlalchemy

def add_versions(request):
    return {
        'python_version': platform.python_version(),
        'django_version': django.get_version(),
        'sqlalchemy_version': sqlalchemy.__version__,
    }
