from django.db import models

# Create your models here.
class Patient (models.Model):
    name =models.CharField('Nome :', max_length=100)
    birth_date =models.DateField('Data de Nascimento')
    gender = models.CharField('Sexo',max_length=1)
    def __str__(self):
        return self.name
class Health_insurance(models.Model):
    name = models.CharField('Nome_Convenio', max_length=150)
    cd_convenio = models.IntegerField('CD_CONVENIO')
    def __str__(self):
        return self.name

class Attendance(models.Model):
    id_patient= models.IntegerField('Cd_Paciente')
    dt_attendance =models.DateField('Data_Atendimento')
    cd_convenio = models.IntegerField('CD_CONVENIO')

    def __str__(self):
        return  f'{self.pk}'

class Convenio(models.Model):
    cd_convenio = models.IntegerField('cd_convenio')
    nm_convenio = models.CharField('nm_convenio', max_length=60)
    sn_fatura_ambulatorio_sus =models.CharField('SN_FATURA_AMBULATORIO_SUS', max_length=1)
    sn_cobra_insumos =models.CharField('SN_COBRA_INSUMOS', max_length=1)
    tp_convenio =models.CharField('TP_CONVENIO', max_length=1)
    cd_for_apre =models.DecimalField('CD_FOR_APRE',decimal_places=2 , max_digits=2)
    tp_forma_agrupamento =models.CharField('TP_FORMA_AGRUPAMENTO', max_length=1)
    tp_importar_matmed =models.CharField('TP_IMPORTAR_MATMED', max_length=1)
    ds_bairro =models.CharField('BAIRRO', max_length=100)
    ds_cidade =models.CharField('CIDADE', max_length=100)
    ds_endereco = models.CharField('ENDERECO', max_length=100)
    ds_uf =models.CharField('UF', max_length=2)
    nr_cgc =models.CharField('CNPJ', max_length=14)
    nr_fone=models.CharField('FONE',max_length=11)
    nr_cep=models.CharField('CEP',max_length=8)
    nm_razao_social =models.CharField('RAZÃO SOCIAL',max_length=60)
    sn_ativo = models.CharField('ATIVO', max_length=1)
    nr_endereco = models.CharField('Nº:' , max_length=10)
    ds_complemento =models.CharField('Complemento' , max_length=60)