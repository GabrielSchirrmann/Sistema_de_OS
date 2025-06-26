from django.db import models

class OrdemServico(models.Model):
    cliente = models.CharField(max_length=100)
    descricao = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[
        ('aberto', 'Aberto'),
        ('em_andamento', 'Em andamento'),
        ('concluido', 'Concluído'),
    ], default='aberto')

    def __str__(self):
        return f"{self.cliente} - {self.status}"
