from django.apps import AppConfig


class CreatewishConfig(AppConfig):
    name = 'createwish'
    
    def ready(self):
        import createwish.signals  # noqa