from django.apps import AppConfig


class HouseConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.house'

    def ready(self):
        import apps.house.signals