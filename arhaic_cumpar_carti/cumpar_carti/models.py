from django.db import models

# Create your models here.

class HeaderParagraf(models.Model):
    titlu = models.CharField(max_length=150)
    paragraf1 = models.TextField()
    paragraf2 = models.TextField()
    slug = models.SlugField(unique=True)
    poza = models.ImageField(upload_to='static/images', null=True)
    
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Header-Paragraf'
        verbose_name_plural = 'Header-Paragrafe'

    def __str__(self) -> str:
        return self.titlu
    
class Paragraf(models.Model):
    titlu = models.CharField(max_length=150)
    paragraf = models.TextField()
    slug = models.SlugField(unique=True)
    poza = models.ImageField(upload_to='static/images', null=True)
    
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Paragraf'
        verbose_name_plural = 'Paragrafe'

    def __str__(self) -> str:
        return self.titlu
    
class Contact(models.Model):
    nume = models.CharField(max_length=50)
    tel = models.CharField(max_length=50)
    email = models.EmailField(None)
    slug = models.SlugField(unique=True)
    
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacte'

    def __str__(self) -> str:
        return self.nume