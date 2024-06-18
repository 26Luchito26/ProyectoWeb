# Generated by Django 4.2.13 on 2024-06-15 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solicitudes', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='solicitudes_epps',
            options={'verbose_name': 'Solicitud de EPP', 'verbose_name_plural': 'Solicitudes de EPPs'},
        ),
        migrations.AlterModelOptions(
            name='solicitudes_material',
            options={'verbose_name': 'Solicitud de material', 'verbose_name_plural': 'Solicitudes de materiales'},
        ),
        migrations.AlterModelOptions(
            name='solicitudes_retiro',
            options={'verbose_name': 'Solicitud de retiro', 'verbose_name_plural': 'Solicitudes de retiros'},
        ),
        migrations.AlterField(
            model_name='solicitudes_epps',
            name='descripcionEpps',
            field=models.CharField(max_length=300, verbose_name='Comentario Adicional - Especifique adecuadamente talla y tipo de vestimenta para todos los EPPs'),
        ),
        migrations.AlterField(
            model_name='solicitudes_epps',
            name='estadoEpps',
            field=models.BooleanField(default=False, verbose_name='EPP verificado'),
        ),
        migrations.AlterField(
            model_name='solicitudes_epps',
            name='fecha_realizarEP',
            field=models.DateField(verbose_name='Fecha de realización'),
        ),
        migrations.AlterField(
            model_name='solicitudes_epps',
            name='nombreEpps',
            field=models.CharField(max_length=100, verbose_name='Nombre del EPP'),
        ),
        migrations.AlterField(
            model_name='solicitudes_epps',
            name='tipo_materialEpps',
            field=models.CharField(choices=[('unitario', 'Unitario'), ('más de un elemento', 'Más de un elemento')], max_length=300, verbose_name='Tipo de material de Epps'),
        ),
        migrations.AlterField(
            model_name='solicitudes_material',
            name='cantidadMaterial',
            field=models.FloatField(verbose_name='Cantidad del material'),
        ),
        migrations.AlterField(
            model_name='solicitudes_material',
            name='descripcionMaterial',
            field=models.CharField(max_length=300, verbose_name='Comentario Adicional - Detalle correctamente los campos, como cantidad y descripción, es crucial para las solicitudes de material'),
        ),
        migrations.AlterField(
            model_name='solicitudes_material',
            name='estadoMaterial',
            field=models.BooleanField(default=False, verbose_name='Material verificado'),
        ),
        migrations.AlterField(
            model_name='solicitudes_material',
            name='fecha_realizarM',
            field=models.DateField(verbose_name='Fecha de realización'),
        ),
        migrations.AlterField(
            model_name='solicitudes_material',
            name='nombre_material',
            field=models.CharField(max_length=100, verbose_name='Nombre del material'),
        ),
        migrations.AlterField(
            model_name='solicitudes_material',
            name='tipo_material',
            field=models.CharField(choices=[('fardo', 'Fardo'), ('kilo', 'Kilo')], max_length=10, verbose_name='Tipo de material'),
        ),
        migrations.AlterField(
            model_name='solicitudes_retiro',
            name='cantidadRetiro',
            field=models.IntegerField(verbose_name='Cantidad a retirar'),
        ),
        migrations.AlterField(
            model_name='solicitudes_retiro',
            name='descripcionRetiro',
            field=models.CharField(max_length=300, verbose_name='Comentario Adicional - Detalle correctamente los campos, como cantidad y descripción, es crucial para las solicitudes de retiro.'),
        ),
        migrations.AlterField(
            model_name='solicitudes_retiro',
            name='estadoRetiro',
            field=models.BooleanField(default=False, verbose_name='Retiro verificado'),
        ),
        migrations.AlterField(
            model_name='solicitudes_retiro',
            name='fecha_realizarR',
            field=models.DateField(verbose_name='Fecha de realización'),
        ),
        migrations.AlterField(
            model_name='solicitudes_retiro',
            name='nombre_retiro',
            field=models.CharField(max_length=100, verbose_name='Nombre del retiro'),
        ),
        migrations.AlterField(
            model_name='solicitudes_retiro',
            name='tipo_materialRetiro',
            field=models.CharField(choices=[('fardo', 'Fardo'), ('kilo', 'Kilo')], max_length=10, verbose_name='Tipo de material de retiro'),
        ),
    ]