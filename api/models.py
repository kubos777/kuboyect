from django.db import models


class Publication(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField('Título ', max_length=100)
    body = models.TextField()

    def __str__(self):
        return 'Título: {0}'.format(self.title)
        