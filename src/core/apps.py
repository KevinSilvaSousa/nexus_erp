from django.apps import AppConfig


class CoreConfig(AppConfig ):  # classe base para configurações de aplicação django
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'
