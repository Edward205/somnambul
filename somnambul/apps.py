from django.apps import AppConfig

class MyAppConfig(AppConfig):
    name = 'somnambul'
    
    def ready(self):
        print("initializare")
