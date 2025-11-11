from django.apps import AppConfig


class UserManagementSystemConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'user_management_system'

    def ready(self):
        import user_management_system.signals # noqa
