from django.apps import AppConfig
from django.db.models import BigAutoField

class HomeConfig(AppConfig):
    default_auto_field = BigAutoField
    name = 'home'
