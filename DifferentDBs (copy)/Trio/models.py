
from django.db import models
from django.utils.translation import gettext_lazy as _

class Trio_data(models.Model):
  title = models.CharField(_("title"), max_length=50,default='')
  company = models.CharField(_("company"), max_length=50,default='',db_column='content')
  app_name = models.CharField(_("app_name"), max_length=50,default='')

  def __str__(self):
    return self.title