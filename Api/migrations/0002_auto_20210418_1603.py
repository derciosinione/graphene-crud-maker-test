# Generated by Django 2.2.4 on 2021-04-18 19:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartaconducao',
            name='entidadeemissoraid',
        ),
        migrations.RemoveField(
            model_name='cartaconducao',
            name='motoristaid',
        ),
        migrations.RemoveField(
            model_name='cartaconducao',
            name='tipocartaconducaoid',
        ),
        migrations.RemoveField(
            model_name='cartoes',
            name='contafinanceiraid',
        ),
        migrations.RemoveField(
            model_name='cartoes',
            name='tipocartaoid',
        ),
        migrations.RemoveField(
            model_name='contactos',
            name='pessoaid',
        ),
        migrations.RemoveField(
            model_name='contactos',
            name='tipocontactoid',
        ),
        migrations.RemoveField(
            model_name='contafinanceira',
            name='bancoid',
        ),
        migrations.RemoveField(
            model_name='contafinanceira',
            name='tipocontaid',
        ),
        migrations.RemoveField(
            model_name='contafinanceira',
            name='titulardacontaid',
        ),
        migrations.RemoveField(
            model_name='distritos',
            name='municipioid',
        ),
        migrations.RemoveField(
            model_name='enderecos',
            name='ruaid',
        ),
        migrations.RemoveField(
            model_name='enderecos',
            name='tipoenderecoId',
        ),
        migrations.RemoveField(
            model_name='moradas',
            name='cidadeid',
        ),
        migrations.RemoveField(
            model_name='moradas',
            name='enderecoid',
        ),
        migrations.RemoveField(
            model_name='motorista',
            name='pessoaid',
        ),
        migrations.RemoveField(
            model_name='pessoa',
            name='estadocivilid',
        ),
        migrations.RemoveField(
            model_name='pessoa',
            name='generoid',
        ),
        migrations.RemoveField(
            model_name='pessoa',
            name='tiposanguineoid',
        ),
        migrations.RemoveField(
            model_name='pessoa',
            name='tituloid',
        ),
        migrations.RemoveField(
            model_name='restricoescategoriascartaconducao',
            name='cartaconducaoid',
        ),
        migrations.RemoveField(
            model_name='restricoescategoriascartaconducao',
            name='restricoescategoriasid',
        ),
        migrations.RemoveField(
            model_name='restricoespessoaiscartaconducao',
            name='cartaconducaoid',
        ),
        migrations.RemoveField(
            model_name='restricoespessoaiscartaconducao',
            name='restricoespessoaisid',
        ),
        migrations.RemoveField(
            model_name='restricoesviaturacartaconducao',
            name='cartaconducaoid',
        ),
        migrations.RemoveField(
            model_name='restricoesviaturacartaconducao',
            name='restricoesviaturaid',
        ),
        migrations.RemoveField(
            model_name='bairros',
            name='distrito_id',
        ),
        migrations.DeleteModel(
            name='Banco',
        ),
        migrations.DeleteModel(
            name='CartaConducao',
        ),
        migrations.DeleteModel(
            name='Cartoes',
        ),
        migrations.DeleteModel(
            name='Contactos',
        ),
        migrations.DeleteModel(
            name='ContaFinanceira',
        ),
        migrations.DeleteModel(
            name='Distritos',
        ),
        migrations.DeleteModel(
            name='Enderecos',
        ),
        migrations.DeleteModel(
            name='EntidadeEmissora',
        ),
        migrations.DeleteModel(
            name='EstadoCivil',
        ),
        migrations.DeleteModel(
            name='Moradas',
        ),
        migrations.DeleteModel(
            name='Motorista',
        ),
        migrations.DeleteModel(
            name='Pessoa',
        ),
        migrations.DeleteModel(
            name='RestricoesCategorias',
        ),
        migrations.DeleteModel(
            name='RestricoesCategoriasCartaConducao',
        ),
        migrations.DeleteModel(
            name='RestricoesPessoais',
        ),
        migrations.DeleteModel(
            name='RestricoesPessoaisCartaConducao',
        ),
        migrations.DeleteModel(
            name='RestricoesViaturaCartaConducao',
        ),
        migrations.DeleteModel(
            name='RestricoesViaturas',
        ),
        migrations.DeleteModel(
            name='TipoContactos',
        ),
        migrations.DeleteModel(
            name='TiposCartaConducao',
        ),
        migrations.DeleteModel(
            name='TiposConta',
        ),
        migrations.DeleteModel(
            name='TiposEndereco',
        ),
        migrations.DeleteModel(
            name='TiposSanguineos',
        ),
        migrations.DeleteModel(
            name='Titulos',
        ),
        migrations.DeleteModel(
            name='TiposCartao',
        ),
    ]
