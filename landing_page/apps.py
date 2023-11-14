from django.apps import AppConfig


class LandingPageConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'landing_page'


    def ready(self):
        import landing_page.signals
