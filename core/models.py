# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Atendime(models.Model):
    cd_atendimento = models.IntegerField(blank=False, null=False , primary_key='cd_atendimento')
    cd_ori_ate = models.BigIntegerField(blank=True, null=True)
    cd_paciente = models.IntegerField(blank=True, null=True)
    cd_convenio = models.IntegerField(blank=True, null=True)
    cd_pro_int = models.CharField(max_length=8, blank=True, null=True)
    cd_pro_int_procedimento_entrad = models.CharField(max_length=8, blank=True, null=True)
    dt_atendimento = models.DateField(blank=True, null=True)
    hr_atendimento = models.DateField(blank=True, null=True)
    tp_atendimento = models.CharField(max_length=1, blank=True, null=True)
    cd_prestador = models.BigIntegerField(blank=True, null=True)
    cd_leito = models.IntegerField(blank=True, null=True)
    cd_loc_trans = models.IntegerField(blank=True, null=True)
    cd_mot_alt = models.IntegerField(blank=True, null=True)
    cd_cid = models.CharField(max_length=6, blank=True, null=True)
    cd_servico = models.IntegerField(blank=True, null=True)
    ds_atendimento = models.CharField(max_length=2000, blank=True, null=True)
    dt_diag = models.DateField(blank=True, null=True)
    dt_alta = models.DateField(blank=True, null=True)
    ds_obs_alta = models.CharField(max_length=2000, blank=True, null=True)
    dt_entrada_same = models.DateField(blank=True, null=True)
    dt_prevista_alta = models.DateField(blank=True, null=True)
    cd_tip_res = models.IntegerField(blank=True, null=True)
    cd_tip_acom = models.IntegerField(blank=True, null=True)
    dt_val_guia = models.DateField(blank=True, null=True)
    nr_guia = models.CharField(max_length=20, blank=True, null=True)
    hr_alta = models.DateField(blank=True, null=True)
    cd_ser_dis = models.IntegerField(blank=True, null=True)
    cd_des_ate = models.BigIntegerField(blank=True, null=True)
    ds_ate_oco = models.CharField(max_length=2000, blank=True, null=True)
    cd_ultimo_mov_int = models.IntegerField(blank=True, null=True)
    cd_casos_atd = models.IntegerField(blank=True, null=True)
    ds_destino_transferencia = models.CharField(max_length=40, blank=True, null=True)
    nm_usuario = models.CharField(max_length=30, blank=True, null=True)
    cd_con_pla = models.IntegerField(blank=True, null=True)
    nm_usuario_alta = models.CharField(max_length=30, blank=True, null=True)
    cd_tipo_internacao = models.IntegerField(blank=True, null=True)
    cd_log_export_atendime = models.IntegerField(blank=True, null=True)
    cd_loc_proced = models.IntegerField(blank=True, null=True)
    cd_log_export_alta = models.IntegerField(blank=True, null=True)
    sn_acompanhante = models.CharField(max_length=1, blank=True, null=True)
    sn_infeccao = models.CharField(max_length=1, blank=True, null=True)
    sn_retorno = models.CharField(max_length=1, blank=True, null=True)
    cd_ssm_cih = models.CharField(max_length=10, blank=True, null=True)
    cd_convenio_secundario = models.IntegerField(blank=True, null=True)
    cd_con_pla_secundario = models.IntegerField(blank=True, null=True)
    cd_multi_empresa = models.IntegerField(blank=True, null=True)
    cd_especialid = models.IntegerField(blank=True, null=True)
    cd_tip_mar = models.IntegerField(blank=True, null=True)
    dt_revisao = models.DateField(blank=True, null=True)
    dt_retorno = models.DateField(blank=True, null=True)
    cd_atendimento_pai = models.IntegerField(blank=True, null=True)
    qt_sessoes = models.IntegerField(blank=True, null=True)
    dt_alta_medica = models.DateField(blank=True, null=True)
    nm_usuario_alta_medica = models.CharField(max_length=30, blank=True, null=True)
    hr_alta_medica = models.DateField(blank=True, null=True)
    cd_servico_saida = models.IntegerField(blank=True, null=True)
    cd_especialid_saida = models.IntegerField(blank=True, null=True)
    cd_loc_trans_saida = models.IntegerField(blank=True, null=True)
    cd_mot_trans_saida = models.IntegerField(blank=True, null=True)
    ds_obs_psih = models.CharField(max_length=2000, blank=True, null=True)
    dt_aviso_medico = models.DateField(blank=True, null=True)
    hr_aviso_medico = models.DateField(blank=True, null=True)
    ds_aviso_tp_contato = models.CharField(max_length=30, blank=True, null=True)
    ds_aviso_obs = models.CharField(max_length=30, blank=True, null=True)
    nm_aviso_usuario = models.CharField(max_length=30, blank=True, null=True)
    tp_programa_alta_unidade = models.CharField(max_length=2, blank=True, null=True)
    ds_programa_alta = models.CharField(max_length=200, blank=True, null=True)
    dt_programa_alta = models.DateField(blank=True, null=True)
    nm_usuario_prog_alta = models.CharField(max_length=30, blank=True, null=True)
    dt_liberacao = models.DateField(blank=True, null=True)
    sn_importa_auto = models.CharField(max_length=1, blank=True, null=True)
    cd_sub_plano = models.CharField(max_length=5, blank=True, null=True)
    sn_busca_ativa = models.CharField(max_length=1, blank=True, null=True)
    tp_busca_ativa = models.CharField(max_length=1, blank=True, null=True)
    sn_obito = models.CharField(max_length=1, blank=True, null=True)
    sn_em_atendimento = models.CharField(max_length=1, blank=True, null=True)
    cd_tip_situacao = models.IntegerField(blank=True, null=True)
    tp_prioridade = models.CharField(max_length=1, blank=True, null=True)
    cd_ssm_sia = models.CharField(max_length=8, blank=True, null=True)
    cd_gru_ate = models.IntegerField(blank=True, null=True)
    sn_consulta_siasus = models.CharField(max_length=1, blank=True, null=True)
    nm_usuario_retorno = models.CharField(max_length=30, blank=True, null=True)
    dt_usuario_retorno = models.DateField(blank=True, null=True)
    sn_recebe_visita = models.CharField(max_length=1, blank=True, null=True)
    nr_chamada_painel = models.CharField(max_length=15, blank=True, null=True)
    nr_laudo = models.BigIntegerField(blank=True, null=True)
    nr_laudo_alto_custo = models.BigIntegerField(blank=True, null=True)
    cd_usuario_diag = models.CharField(max_length=40, blank=True, null=True)
    cd_usuario_upd_diag = models.CharField(max_length=40, blank=True, null=True)
    dt_ultima_upd_diag = models.DateField(blank=True, null=True)
    nr_pedido_laudo = models.BigIntegerField(blank=True, null=True)
    cd_escala_dia = models.IntegerField(blank=True, null=True)
    hr_agenda = models.DateField(blank=True, null=True)
    cd_tip_acom_cobertura = models.IntegerField(blank=True, null=True)
    cd_setor_obito = models.IntegerField(blank=True, null=True)
    dt_solic_medica = models.DateField(blank=True, null=True)
    nr_seq_preimpre = models.BigIntegerField(blank=True, null=True)
    sn_atendimento_apac = models.CharField(max_length=1, blank=True, null=True)
    sn_obito_infec = models.CharField(max_length=1, blank=True, null=True)
    dt_chegada_paciente = models.DateField(blank=True, null=True)
    nr_carteira = models.CharField(max_length=25, blank=True, null=True)
    dt_validade = models.DateField(blank=True, null=True)
    nm_empresa = models.CharField(max_length=30, blank=True, null=True)
    nr_carteira_acoplamento = models.CharField(max_length=25, blank=True, null=True)
    dt_validade_acoplamento = models.DateField(blank=True, null=True)
    nm_empresa_acoplamento = models.CharField(max_length=30, blank=True, null=True)
    nr_declaracao_obito = models.CharField(max_length=11, blank=True, null=True)
    senha_sus = models.CharField(max_length=20, blank=True, null=True)
    hr_atendimento_medico = models.DateField(blank=True, null=True)
    cd_seq_integra = models.CharField(max_length=20, blank=True, null=True)
    dt_integra = models.DateField(blank=True, null=True)
    sn_paciente_paga_dif_diaria = models.CharField(max_length=1, blank=True, null=True)
    cd_guia = models.IntegerField(blank=True, null=True)
    cd_laudo_apac = models.IntegerField(blank=True, null=True)
    tp_doenca = models.CharField(max_length=1, blank=True, null=True)
    nr_tempo_doenca = models.IntegerField(blank=True, null=True)
    tp_tempo_doenca = models.CharField(max_length=1, blank=True, null=True)
    tp_carater_internacao = models.CharField(max_length=1, blank=True, null=True)
    tp_obito_mulher = models.BooleanField(blank=True, null=True)
    tp_acidente_tiss = models.BooleanField(blank=True, null=True)
    cd_atendimento_sus_vinculado = models.IntegerField(blank=True, null=True)
    tp_atendimento_tiss = models.IntegerField(blank=True, null=True)
    sn_gestacao_tiss = models.CharField(max_length=1, blank=True, null=True)
    sn_aborto_tiss = models.CharField(max_length=1, blank=True, null=True)
    sn_transtorno_tiss = models.CharField(max_length=1, blank=True, null=True)
    sn_complicacao_tiss = models.CharField(max_length=1, blank=True, null=True)
    sn_atend_neo_tiss = models.CharField(max_length=1, blank=True, null=True)
    sn_complicacao_neo_tiss = models.CharField(max_length=1, blank=True, null=True)
    sn_baixo_peso_tiss = models.CharField(max_length=1, blank=True, null=True)
    sn_cesario_tiss = models.CharField(max_length=1, blank=True, null=True)
    sn_recem_nato = models.CharField(max_length=1, blank=True, null=True)
    sn_notificar_policia = models.CharField(max_length=1, blank=True, null=True)
    sn_custodia_policial = models.CharField(max_length=1, blank=True, null=True)
    cd_cid_obito = models.CharField(max_length=6, blank=True, null=True)
    sn_normal_tiss = models.CharField(max_length=1, blank=True, null=True)
    sn_paga_acompanhante = models.CharField(max_length=1, blank=True, null=True)
    cd_setor_local_fscc = models.IntegerField(blank=True, null=True)
    sn_pacote = models.CharField(max_length=1, blank=True, null=True)
    sn_pacote_day_clinic = models.CharField(max_length=1, blank=True, null=True)
    nr_guia_envio_principal = models.CharField(max_length=20, blank=True, null=True)
    cd_procedimento = models.CharField(max_length=10, blank=True, null=True)
    cd_cbo_prestador = models.CharField(max_length=6, blank=True, null=True)
    cd_carater_atendimento = models.IntegerField(blank=True, null=True)
    cd_atendimento_integra = models.CharField(max_length=50, blank=True, null=True)
    cd_procedimento_alta = models.CharField(max_length=10, blank=True, null=True)
    cd_prestador_em_atendimento = models.CharField(max_length=30, blank=True, null=True)
    sn_relacao_trabalho = models.CharField(max_length=1, blank=True, null=True)
    sn_suspeita_epidemia = models.CharField(max_length=1, blank=True, null=True)
    sn_reavaliacao = models.CharField(max_length=1, blank=True, null=True)
    nr_tag_atendimento = models.CharField(max_length=20, blank=True, null=True)
    sn_internado = models.CharField(max_length=1, blank=True, null=True)
    nr_pre_natal = models.CharField(max_length=20, blank=True, null=True)
    nr_autorizacao_gestor = models.CharField(max_length=13, blank=True, null=True)
    tp_encaminhamento_obito = models.CharField(max_length=5, blank=True, null=True)
    cd_protocolo = models.BigIntegerField(blank=True, null=True)
    cd_sintoma_avaliacao = models.BigIntegerField(blank=True, null=True)
    vl_escore = models.BigIntegerField(blank=True, null=True)
    cd_cor_referencia = models.BigIntegerField(blank=True, null=True)
    cd_res_lei_regulacao = models.IntegerField(blank=True, null=True)
    cd_meio_transporte = models.IntegerField(blank=True, null=True)
    dh_alta_medica_lancada = models.DateField(blank=True, null=True)
    dh_alta_lancada = models.DateField(blank=True, null=True)
    nm_usuario_autorizador = models.CharField(max_length=30, blank=True, null=True)
    cd_atendimento_original = models.FloatField(blank=True, null=True)
    sn_seguro_complementar = models.CharField(max_length=1, blank=True, null=True)
    sn_retencao_judicial = models.CharField(max_length=1, blank=True, null=True)
    cd_sistema = models.CharField(max_length=6, blank=True, null=True)
    cd_programas_homecare = models.FloatField(blank=True, null=True)
    cd_atendimento_tiss = models.FloatField(blank=True, null=True)
    tp_cobertura_especial = models.CharField(max_length=2, blank=True, null=True)
    tp_saude_ocupacional = models.CharField(max_length=2, blank=True, null=True)
    tp_regime_atendimento = models.CharField(max_length=2, blank=True, null=True)

    def __str__(self):
        return f'{self.cd_atendimento}'

    class Meta:
        managed = True
        db_table = 'atendime'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128, blank=True, null=True)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150, blank=True, null=True)
    first_name = models.CharField(max_length=150, blank=True, null=True)
    last_name = models.CharField(max_length=150, blank=True, null=True)
    email = models.CharField(max_length=254, blank=True, null=True)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Convenio(models.Model):
    cd_convenio = models.IntegerField(primary_key=True)
    nm_convenio = models.CharField(max_length=60, blank=True, null=True)
    sn_fatura_ambulatorio_sus = models.CharField(max_length=1, blank=True, null=True)
    sn_cobra_insumos = models.CharField(max_length=1, blank=True, null=True)
    tp_convenio = models.CharField(max_length=1, blank=True, null=True)
    cd_for_apre = models.IntegerField(blank=True, null=True)
    tp_forma_agrupamento = models.CharField(max_length=1, blank=True, null=True)
    tp_importar_matmed = models.CharField(max_length=1, blank=True, null=True)
    ds_bairro = models.CharField(max_length=100, blank=True, null=True)
    ds_cidade = models.CharField(max_length=100, blank=True, null=True)
    ds_endereco = models.CharField(max_length=100, blank=True, null=True)
    ds_uf = models.CharField(max_length=2, blank=True, null=True)
    nr_cgc = models.CharField(max_length=14, blank=True, null=True)
    nr_fone = models.CharField(max_length=11, blank=True, null=True)
    nr_cep = models.CharField(max_length=8, blank=True, null=True)
    nm_razao_social = models.CharField(max_length=60, blank=True, null=True)
    sn_ativo = models.CharField(max_length=1, blank=True, null=True)
    nr_endereco = models.CharField(max_length=10, blank=True, null=True)
    ds_complemento = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'convenio'


class CoreConvenio(models.Model):
    id = models.BigAutoField(primary_key=True)
    cd_convenio = models.IntegerField()
    nm_convenio = models.CharField(max_length=60, blank=True, null=True)
    sn_fatura_ambulatorio_sus = models.CharField(max_length=1, blank=True, null=True)
    sn_cobra_insumos = models.CharField(max_length=1, blank=True, null=True)
    tp_convenio = models.CharField(max_length=1, blank=True, null=True)
    cd_for_apre = models.DecimalField(max_digits=38, decimal_places=2)
    tp_forma_agrupamento = models.CharField(max_length=1, blank=True, null=True)
    tp_importar_matmed = models.CharField(max_length=1, blank=True, null=True)
    ds_bairro = models.CharField(max_length=100, blank=True, null=True)
    ds_cidade = models.CharField(max_length=100, blank=True, null=True)
    ds_endereco = models.CharField(max_length=100, blank=True, null=True)
    ds_uf = models.CharField(max_length=2, blank=True, null=True)
    nr_cgc = models.CharField(max_length=14, blank=True, null=True)
    nr_fone = models.CharField(max_length=11, blank=True, null=True)
    nr_cep = models.CharField(max_length=8, blank=True, null=True)
    nm_razao_social = models.CharField(max_length=60, blank=True, null=True)
    sn_ativo = models.CharField(max_length=1, blank=True, null=True)
    nr_endereco = models.CharField(max_length=10, blank=True, null=True)
    ds_complemento = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'core_convenio'


class CoreHealthInsurance(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=150, blank=True, null=True)
    cd_convenio = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'core_health_insurance'


class CorePatient(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    birth_date = models.DateField()
    gender = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'core_patient'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200, blank=True, null=True)
    action_flag = models.IntegerField()
    change_message = models.TextField(blank=True, null=True)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100, blank=True, null=True)
    model = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField(blank=True, null=True)
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
