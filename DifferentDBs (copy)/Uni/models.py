from django.db import models
from django.utils.translation import gettext_lazy as _

class Uni_data(models.Model):
  user_name = models.CharField(_("user"), max_length=50,default='')
  email_id = models.EmailField(_("email"), max_length=50,default='')

  def __str__(self):
    return self.user_name