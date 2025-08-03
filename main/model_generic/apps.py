from django.apps import AppConfig


class ModelGenericConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'model_generic'
