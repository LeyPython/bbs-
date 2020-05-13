from django.apps import AppConfig
from django.utils.module_loading import autodiscover_modules



class BbsConfig(AppConfig):
    name = 'bbs'

    def ready(self):
        autodiscover_modules("stark")