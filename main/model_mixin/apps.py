from django.apps import AppConfig


class ModelMixinConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'model_mixin'
