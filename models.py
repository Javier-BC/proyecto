from django.db import models
from django.contrib.auth.models import User

class calendario(models.Model):
    titulo = models.CharField(max_length=40)
    snippet = models.CharField(max_length=150, blank=True)
    cuerpo = models.TextField(max_length=10000, blank=True)
    creado = models.DateTimeField(auto_now_add=True)
    fecha = models.DateField(blank=True)
    creador = models.ForeignKey(User, blank=True, null=True)
    remind = models.BooleanField(default=False)

    def __unicode__(self):
        if self.titulo:
            return unicode(self.creador) + u" - " + self.titulo
        else:
            return unicode(self.creador) + u" - " + self.snippet[:40]

    def short(self):
        if self.snippet:
            return u"<i>%s</i> - %s" % (self.titulo, self.snippet)
        else:
            return self.titulo
    short.allow_tags = True

    class Meta:
        verbose_name_plural = "calendarios"
