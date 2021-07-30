from django.db import models
from django.conf import settings

class DBRouter(object):
    """
    A router to control all database operations on models in the
    user application.
    """
    def db_for_read(self, model, **hints):
        return settings.DATABASE_APPS_MAPPING.get(model._meta.model_name, None)

    def db_for_write(self, model, **hints):
        return settings.DATABASE_APPS_MAPPING.get(model._meta.model_name, None)

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the user app is involved.
        """
        db1 = settings.DATABASE_APPS_MAPPING.get(obj1._model_name)
        db2 = settings.DATABASE_APPS_MAPPING.get(obj2._model_name)
        if db1 and db2:
            return db1 == db2
        return None

    def allow_migrate(self, db, app_label, model_name, **hints):
        if db in settings.DATABASE_APPS_MAPPING.values():
            return settings.DATABASE_APPS_MAPPING.get(model_name) == db
        return None




# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=100,default='')
    # class Meta():
    #     app_label = 'user_data'
    def __str__(self):
        return self.username

class Customer(models.Model):
    name = models.TextField(max_length=100,default='')
    
    # class Meta():
    #     app_label = 'customer_data'

    def __str__(self):
        return self.name