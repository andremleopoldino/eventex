from django.db import models


class Subscriptions(models.Model):
    name = models.CharField('nome', max_length=100)
    cpf = models.CharField(max_length=11)
    email = models.EmailField()
    phone = models.CharField('telefone' , max_length=20)
    created_at = models.DateTimeField('Inscrição realizada em : ' , auto_now_add=True)
    

    class Meta:
        verbose_name_plural =   'inscrições'
        verbose_name = 'inscrição'
        ordering = ('-created_at',)

    def __str__(self):
        return self.name

    
    