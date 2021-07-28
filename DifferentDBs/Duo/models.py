from django.db import models
from django.utils.translation import gettext_lazy as _

class DuoData(models.Model):
  membership = models.BooleanField(_("membership"), default=False)
  customer = models.CharField(_("customer"), max_length=50,default='')
  app_name = models.CharField(_("app_name"), max_length=50,default='')

  def __str__(self):
    return self.customer