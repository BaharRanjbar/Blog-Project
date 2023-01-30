from django.db import models
from django.utils.translation import gettext as _


class Postblog(models.Model):
      
    STATUS_CHOICES =(
    ('pub' , 'Published'),
    ('drf' , 'Draft'),
)
    
    title = models.CharField(_("نام بلاگ"), max_length=50)
    text = models.TextField(_("متن بلاگ"))
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    datetime_created = models.DateTimeField(_("تاریخ و ساعت ثبت"),auto_now_add=True)
    datetime_modified = models.DateTimeField(_("تاریخ و ساعت ویرایش"), auto_now=True)
    status= models.CharField(_("وضعیت"),choices= STATUS_CHOICES, max_length=3)

    
    def __str__(self):
        return self.title
