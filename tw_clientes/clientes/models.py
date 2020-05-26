from django.db import models

class Endereco(models.Model):
    ESTADOS_CHOICES = (
        ("AC","Acre"), ("AL", "Alagoas"), ("AM","Amazonas"), ("AP","Amapá"),
        ("BA", "Bahia"), ("CE","Ceará"), ("DF","Distrito Federal"), ("ES","Espírito Santo"),
        ("GO", "Goiás"), ("MA","Maranhão"), ("MG","Minas Gerais"), ("MS","Mato Grosso do Sul"),
        ("MT","Mato Grosso"), ("PA","Pará"), ("PB","Paraíba"), ("PE","Pernambuco"), ("PI","Piauí"), ("PR","Paraná"),
        ("RJ","Rio de Janeiro"), ("RN","Rio Grande do Norte"), ("RO","Rondônia"), ("RR","Roraima"),
        ("RS","Rio Grande do Sul"), ("SC","Santa Catarina"), ("SE","Sergipe"), ("SP","São Paulo"), ("TO","Tocantins"),

    )
    rua = models.CharField(max_length=100,null=False,blank=False)
    numero = models.IntegerField(null=False, blank=False)
    complemento = models.CharField(max_length=200,null=False,blank=False)
    bairro = models.CharField(max_length=100,null=False,blank=False)
    cidade = models.CharField(max_length=100,null=False,blank=False)
    estado = models.CharField(max_length=2, choices=ESTADOS_CHOICES,blank=False,null=False)
    pais = models.CharField(max_length=100,null=False,blank=False)

    def __str__(self):
        return self.rua

# Create your models here.
class Cliente(models.Model):

    SEXO_CHOICES = (
        ("F","Feminino"),
        ("M", "Masculino"),
        ("N","Nenhum dos dois")
    )
    nome = models.CharField(max_length=100,null=False,blank=False)
    data_nascimento = models.DateField(null=False, blank=False)
    email = models.EmailField(null=False,blank=False)
    profissao = models.CharField(max_length=50,null=False,blank=False)
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES,blank=False,null=False)
    endereco = models.OneToOneField(Endereco, on_delete=models.SET_NULL,null=True)

    #exibe o nome e não o objeto
    def __str__(self):
        return self.nome

