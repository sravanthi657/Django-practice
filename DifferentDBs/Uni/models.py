from django.db import models
from django.utils.translation import gettext_lazy as _


class MapRouter:
    """
    A router to control all database operations on models in the
    user application.
    """
    def db_for_read(self, model, **hints):
        """
        Attempts to read user models go to default.
        """
        if model._meta.app_label == 'Uni_data':
            return 'default'
        elif model._meta.app_label == 'Register_data':
            return 'details_db'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write user models go to default.
        """
        if model._meta.app_label == 'Uni_data':
            return 'default'
        elif model._meta.app_label == 'Register_data':
            return 'details_db'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the user app is involved.
        """
        if obj1._meta.app_label == 'Uni_data' or \
           obj2._meta.app_label == 'Uni_data':
           return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the auth app only appears in the 'default'
        database.
        """
        if app_label == 'Uni_data':
            return db == 'default'
        return None



class Uni_data(models.Model):
  user_name = models.CharField(_("user"), max_length=50,default='')
  email_id = models.EmailField(_("email"), max_length=50,default='')

  def __str__(self):
    return self.user_name

class Register_data(models.Model):
    Fullname = models.TextField(_("FullName"),max_length=100,default='')

    def __str__(self):
      return self.Fullname