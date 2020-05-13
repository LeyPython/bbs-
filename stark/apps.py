from django.apps import AppConfig
from django.utils.module_loading import autodiscover_modules

class StarkConfig(AppConfig):
    name = 'stark'

    # 程序启动时，就执行app下得stark.py文件
    def ready(self):
        autodiscover_modules('stark')
