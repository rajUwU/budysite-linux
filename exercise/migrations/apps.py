from django.apps import AppConfig


class ExerciseConfig(AppConfig):
    name = 'exercise'

    def ready(self):
        from exercise import signals
