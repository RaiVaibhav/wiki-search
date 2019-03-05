from django.db import models

class Pdfbyte(models.Model):
    name = models.CharField(max_length=1000, unique=True, primary_key=True)
    bytedata = models.BinaryField()

    def __str__(self):
        return self.name