from django.contrib import admin

from .models import *

class PattientAdmin(admin.ModelAdmin):
    list_display = ('name', 'birth_date', 'gender')

class ConvenioAdmin(admin.ModelAdmin):
    list_display = ('cd_convenio', 'nm_convenio', 'sn_ativo')

class AtendimeAdmin(admin.ModelAdmin):
    list_display = ('cd_atendimento', 'cd_paciente','cd_convenio')
    actions = ('export_csv')


admin.site.register(Atendime, AtendimeAdmin)

admin.site.register(Convenio, ConvenioAdmin)