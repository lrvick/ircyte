from django.db import models
from django.db import connection 
from django.template.defaultfilters import striptags

class Log(models.Model):
    """
    A single message logged. Because of type it could theoretically be anything, action, quote etc.
    """
    nick = models.CharField(max_length=255, help_text='An IRC users nick.')
    created = models.DateTimeField(auto_now=True, help_text="When this was created.")
    msg = models.TextField(help_text='An IRC message.')
    type = models.CharField(max_length=255, help_text="Type of message. Since this is a charfield, it can really be anything.")
    channel = models.CharField(max_length=255, help_text="The channel this was said in. ex. #adullam")

    class Meta:
        verbose_name = "Log Entry"
        verbose_name_plural = "Log Entries"
        ordering = ('-id',)

    def __unicode__(self):
        return self.nick 

